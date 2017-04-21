#include <wiringPi.h>

static int firstPin = 4;
static int lastPin = 15;
static int keyPins[16] =
{
	0,
	0,
	0,
	0,
	12, //10
	13, //9
	14, //11
    21, //5
    22, //6
    23, //13
    24, //19
    25, //26
    27, //16
    28, //20
    26, //12
	0
};

void pout(int x, int y)
{
	digitalWrite(keyPins[x],y);
}

void poutL(int x)
{
	pout(x, 0);
}

void poutH(int x)
{
	pout(x, 1);
}

void poutB(int x, int z)
{
	if (z)
		pout(x, 1);
	else
		pout(x, 0);
}

//#define pout(x, y) digitalWrite(keyPins[x],(y))
//#define poutL(x) pout(x, 0)
//#define poutH(x) pout(x, 1)
//#define poutB(a, z) pout(a, ((z)?1:0))


void init (void)
{
    poutL(9);    
    poutL(10);    
    poutH(11);    
    poutH(12);
    poutH(6);    
    delay(1); 

    poutL(6);    
    poutL(9);    
    poutL(10);    
    poutL(11);    
    poutL(12);
    delay(1); 
}

void setCursor(int f, int b, int a)
{
    pout(7,f);
    pout(8,b);
    pout(9,a);
    poutH(10);
    poutH(6);
    delay(1); 

    poutL(6);
    poutL(7);
    poutL(8);
    poutL(9);
    poutL(10);
    delay(1); 
}

void mdfs(int p)
{
    poutH(p);
    poutH(6);
    delay(1);

    poutL(6);
    poutL(p);
    delay(1);
}

void scrollScreen()
{
    poutH(9);
    poutH(10);
    poutH(11);
    poutH(6);
    delay(1);

    poutL(6);
    poutL(9);
    poutL(10);
    poutL(11);
    delay(1);
}

void outputChar(int c)
{
    poutH(4);
    
    poutB(7, c & 1);
    poutB(8, c & 2);
    poutB(9, c & 4);
    poutB(10, c & 8);

    poutB(11, c & 16);
    poutB(12, c & 32);
    poutB(13, c & 64);
    poutB(14, c & 128);

    poutH(6);
    delay(1);

    poutL(6);
    poutL(4);

    poutL(7);
    poutL(8);
    poutL(9);
    poutL(10);

    poutL(11);
    poutL(12);
    poutL(13);
    poutL(14);

	delay(1);

}
void displayStart()
{
wiringPiSetup();
    for (int i = firstPin; i < lastPin; i++)
    {
		pinMode(keyPins[i], OUTPUT);
		digitalWrite(keyPins[i], LOW);
    }
    init();
    setCursor(LOW,LOW,LOW);
    mdfs(7);
    //mdfs(9); //entry mode set
    mdfs(8);
    setCursor(LOW,LOW,HIGH);
    mdfs(14); //ddram osoiute
}


void displayClear()
{
    init();
    setCursor(LOW,LOW,LOW);
    mdfs(7);
    //mdfs(9); //entry mode set
    mdfs(8);
    setCursor(LOW,LOW,HIGH);
    mdfs(14); //ddram osoiute
}

void displayPrint(const char* str)
{

	while (*str)
	{
		outputChar(*str);
		str++;
	}
}

int main (int argc, const char** argv)
{
	displayStart();
argc--;
argv++;
    while(argc--)
	{
		const char* dd = argv[0];
		displayClear();
		displayPrint(dd);
		argv++;
	}
	return 0 ;
}
