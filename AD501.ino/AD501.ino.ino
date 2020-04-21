/************************************************************************
32 * 16 LED MATRIX AD-501-C:
               1:VCC    pin -> 3V3
               2:SIN1   pin -> IO25
               3:SIN2   pin -> IO26
               4:SIN3   pin -> IO15
               5:CLOCK  pin -> IO14
               6:LATCH  pin -> IO12
               7:ENABLE pin -> IO13
               8:VLED   pin  -> 3V3
               9:GND    pin  -> GND
              10:GND    pin  -> GND
**************************************************************************/
#define SIN1 10
#define SIN2 11
#define SIN3 23
#define CLOCK 13
#define LATCH 14
#define ENABLE 16

word DisplayBuffer[32];
byte Displayi = 0;
byte anime[4][32];
byte anime_wk[4];
int i, j;

short HourH, HourL, MinH, MinL, Sec;
boolean  HourHF, HourLF, MinHF;
unsigned long Millisecond = 0;
int Anime_cnt;
int Anime_no;
int in_Year;
int in_Month;
int in_Day;
int in_Hour;
int in_Minute;
int in_Second;
int buffer_length;
char buff[30];

void setup() {
  // put your setup code here, to run once:
  pinMode(SIN1, OUTPUT);
  pinMode(SIN2, OUTPUT);
  pinMode(SIN3, OUTPUT);
  pinMode(CLOCK, OUTPUT);
  pinMode(LATCH, OUTPUT);
  pinMode(ENABLE, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

}

void Led32x16Display()
{
  byte j;
  Millisecond++;
  Displayi < 16 ? Displayi++ : Displayi = 0;
  for (j = 0; j < 16; j++) {
    digitalWrite(SIN1, ( 0x8000 >> Displayi >> j ) & 0x0001);
    digitalWrite(SIN2, (*(DisplayBuffer + 15 - j) >> 15 - Displayi) & 0x0001 );
    digitalWrite(SIN3, (*(DisplayBuffer + 31 - j) >> 15 - Displayi) & 0x0001 );
    digitalWrite(CLOCK, LOW);
    digitalWrite(CLOCK, HIGH);
  }
  digitalWrite(LATCH, HIGH);
  digitalWrite(LATCH, LOW);
}
