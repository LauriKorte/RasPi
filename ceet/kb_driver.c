#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <wiringPi.h>

#define KEYBOARD_COLUMNS 3
#define KEYBOARD_ROWS 4

static int keyCols[KEYBOARD_COLUMNS] =
{
	5,
	16,
	1
};

static int keyRows[KEYBOARD_ROWS] =
{
	0,
	2,
	3,
	4
};

unsigned waitingFirst = 0;
unsigned waitingLast = 0;
int* buffer = 0;
size_t currentBufferSize = 0;

#define INITIAL_BUFFER_SIZE 500
#define BUFFER_CLEAR_THRESHOLD 250

pthread_t driverThread;
pthread_mutex_t bufferMutex;

pthread_cond_t eventsQueued;

static void internal_allocateBuffer()
{
	if (buffer == 0)
	{
		buffer = malloc(INITIAL_BUFFER_SIZE * sizeof(int));
		waitingFirst = 0;
		waitingLast = 0;
		currentBufferSize = INITIAL_BUFFER_SIZE;
		
		printf("Allocated initial buffer %p with %x places\n", buffer, (unsigned int) currentBufferSize);
	}
	else
	{
		if (waitingFirst >= BUFFER_CLEAR_THRESHOLD)
		{
			int* newBuffer = malloc(currentBufferSize * sizeof(int));
			memcpy(newBuffer, buffer + waitingFirst, (currentBufferSize - waitingFirst) * sizeof(int));
			free(buffer);
			
			buffer = newBuffer;
			
			waitingLast -= waitingFirst;
			waitingFirst = 0;
		
			printf("Buffer copied to %p\n", buffer);
		}
		else
		{
			buffer = realloc(buffer, currentBufferSize * 2 * sizeof(int));
			currentBufferSize = currentBufferSize * 2;
			printf("Buffer reallocated to %p with %x places\n", buffer, (unsigned int) currentBufferSize);
		}
	}

}

void addEvent(int event)
{
    pthread_mutex_lock (&bufferMutex);
	printf("Adding event %x\n", (unsigned int) event);
	
	if (waitingLast >= currentBufferSize-1)
	{
		internal_allocateBuffer();
	}
	buffer[waitingLast] = event;
	waitingLast += 1;
		
	pthread_cond_broadcast(&eventsQueued);
	pthread_mutex_unlock (&bufferMutex);
}
int waitEvent()
{
	int retEvent = 0;
	
    	pthread_mutex_lock (&bufferMutex);
	
	while (waitingLast <= waitingFirst)
	{
		pthread_cond_wait(&eventsQueued, &bufferMutex);
	}
	retEvent = buffer[waitingFirst];
	waitingFirst += 1;	

	printf("Waited for event %x\n", (unsigned int) retEvent);

	pthread_mutex_unlock (&bufferMutex);
	
	return retEvent;
}

int readEvent()
{
	int retEvent = 0;
	
	
    	pthread_mutex_lock (&bufferMutex);
	
	if (waitingLast >= waitingFirst)
	{
		retEvent = buffer[waitingFirst];
		waitingFirst += 1;
	}
	
	printf("Read event %x\n", (unsigned int) retEvent);
    	pthread_mutex_unlock (&bufferMutex);
	
	return retEvent;
}

#define KEY_MASK 0xFF
#define KEY_STATUS_SHIFT 8

int keyboardStatus[KEYBOARD_ROWS * KEYBOARD_COLUMNS];

int getKeyStatus(int row, int col)
{
	return keyboardStatus[row + col * KEYBOARD_ROWS];
}

void setKeyStatus(int row, int col, int stat)
{
	keyboardStatus[row + col * KEYBOARD_ROWS] = stat;
}

#define DRIVER_COLUMN_WAIT delayMicroseconds(120)

int driverStatus = 0;

void* driverLoop(void* thrdparams)
{
	wiringPiSetup();
	
	for (int i = 0; i < KEYBOARD_ROWS*KEYBOARD_COLUMNS; i++)
		keyboardStatus[i] = 0;

	for (int i = 0; i < KEYBOARD_COLUMNS; i++)
	{
		pinMode(keyCols[i], OUTPUT);
		digitalWrite(keyCols[i], LOW);
	}

	for (int i = 0; i < KEYBOARD_ROWS; i++)
	{
		pinMode(keyRows[i], INPUT);
	}

	pthread_mutex_lock (&bufferMutex);
	
	internal_allocateBuffer();

	pthread_cond_broadcast(&eventsQueued);

	pthread_mutex_unlock (&bufferMutex);


	while(driverStatus)
	for (int i = 0; i < KEYBOARD_COLUMNS; i++)
	{
		digitalWrite(keyCols[i], HIGH);
		DRIVER_COLUMN_WAIT;

		for (int i2 = 0; i2 < KEYBOARD_ROWS; i2++)
		{
			int status = digitalRead(keyRows[i2]);
			if (getKeyStatus(i2, i) != status)
			{
				setKeyStatus(i2, i, status);
				addEvent(i2 + i * KEYBOARD_ROWS + (status << KEY_STATUS_SHIFT));
			}
		}

		digitalWrite(keyCols[i], LOW);
		DRIVER_COLUMN_WAIT;
	}
	pthread_exit(NULL);
}

void endDriver()
{
	if (driverStatus == 0)
	{
		printf("Error, driver not running");
		return;
	}
	driverStatus = 0;
	pthread_join(driverThread, NULL);
}

void startDriver()
{
	if (driverStatus == 1)
	{
		printf("Error, driver already running");
		return;
	}
	driverStatus = 1;
	pthread_cond_init(&eventsQueued, NULL);
	pthread_mutex_lock (&bufferMutex);

	pthread_create(&driverThread, NULL, driverLoop, NULL);
	pthread_cond_wait(&eventsQueued, &bufferMutex);

	pthread_mutex_unlock (&bufferMutex);
}


int main (int argc, char *argv[])
{
	startDriver();
	int i = 0;
	while(i = waitEvent())
	{
	}
	endDriver();
}
