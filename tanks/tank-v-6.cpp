//  This is a simple code for an autonomus Arduino car/ tank.
#include<SPI.h>
#include<MFRC522.h>
#define RST_PIN 49
#define SS_PIN  53
MFRC522 mfrc522(SS_PIN, RST_PIN); // CREATING MFRC522 instance
String read_rfid;
String start_tank  = "6d6ae2e3";
#define led 42
#define trigR 11
#define echoR 9
#define pinkanon 42
#define trigB 12
#define echoB 13
#define trigL 10
#define echoL 8
#define Green 46
#define Yellow 48
#define Red 46
#define ena 7
#define in2 6
#define in3 5
#define in4 4
#define in1 3
#define ena1 2
int SPEED_Right;
int SPEED_Left;
int SPEED_Right_Revers;
int SPEED_Left_Revers;
float durationR, distanceR, distanceL, durationL, durationB, distanceB;
  //------------------------------------------------------------------------
void setup(){
  Serial.begin(9600);
  SPI.begin(); // initialize SPI bus
  mfrc522.PCD_Init(); // initilize MFRC522 card
  pinMode(led, OUTPUT);
  //------------------------------------------------------------------------
   pinMode(trigR, OUTPUT);
   pinMode(echoR, INPUT);
   pinMode(trigB, OUTPUT);
   pinMode(echoB, INPUT);
   pinMode(trigL, OUTPUT);
   pinMode(echoL, INPUT);
   pinMode(Green, OUTPUT);
   pinMode(Yellow, OUTPUT);
   pinMode(Red, OUTPUT);
   pinMode(ena, OUTPUT);
   pinMode(in4, OUTPUT);
   pinMode(in3, OUTPUT);
   pinMode(ena1, OUTPUT);
   pinMode(in2, OUTPUT);
   pinMode(in1, OUTPUT);
   //color(0,0,255);

}
 //------------------------------------------------------------------------

 void color(int R, int G, int Y){
  analogWrite(Red, R);
  analogWrite(Green, G);
  analogWrite(Yellow, Y);
 }
  //------------------------------------------------------------------------
 

void byte_array(byte * buff, byte buff_size){
  read_rfid="";
  for (byte i = 0; i<buff_size; i++){
    read_rfid = read_rfid + String(buff[i], HEX);
    
  }
}

  //------------------------------------------------------------------------

void READ_CARD_AND_START_TANK(){
  // Front Right
  digitalWrite(trigR, LOW);
  delayMicroseconds(1);
  digitalWrite(trigR, HIGH);
  delayMicroseconds(1);
  digitalWrite(trigR, LOW);
  durationR = pulseIn(echoR, HIGH);
  distanceR = (durationR/2)* 0.0343;

// Front LEFT
  digitalWrite(trigL, LOW);
  delayMicroseconds(1);
  digitalWrite(trigL, HIGH);
  delayMicroseconds(1);
  digitalWrite(trigL, LOW);
  durationL = pulseIn(echoL, HIGH);
  distanceL = (durationL/2)* 0.0343;
  
// REVERS
  digitalWrite(trigB, LOW);
  delayMicroseconds(1);
  digitalWrite(trigB, HIGH);
  delayMicroseconds(1);
  digitalWrite(trigB, LOW);
  durationB = pulseIn(echoB, HIGH);
  distanceB = (durationB/2)* 0.0343;
  //------------------------------------------------------------------------

     
  if(distanceR >=400 && distanceR < 4 && distanceL >=400 && distanceL < 4 && distanceB>=400 && distanceB<4){
    Serial.println("Out of range");
    color(255,0,0);       //    RED   
    color(255,255,0);       //YELLOW
    color(0,255,0);       //  LIME
  //  servo();

   }else if(distanceR >=360 || distanceR < 4){
    Serial.println("Out of range RIGHT");
    color(0, 0, 255);       //  BLUE
    color(255, 140, 0);     // DARKORANGE
    }else if(distanceL >=360 || distanceL < 4){
    Serial.println("Out of range LEFT");
     color(0, 0, 255);       //  BLUE
    color(255, 140, 0);     // DARKORANGE
    }else if(distanceB>=360 || distanceB<4){
     Serial.println("Out of range REVRS");
    color(0, 191, 255);       //  DEEPSKYBLUE
    color(128, 0, 128);     // PURPLE

    }   //------------------------------------------------------------------------

     else{
     Serial.print("Distance Front LEET = ");
     Serial.print(distanceL);
     Serial.println(" cm");
     
     Serial.print("Distnace Front RIGHT = ");
     Serial.print(distanceR);
     Serial.println(" cm");

     Serial.print("Distance Revers = ");
     Serial.print(distanceB);
     Serial.println(" cm");
     
     delayMicroseconds(1);
     //------------------------------------------------------------------------

     if(distanceR >=350 && distanceL >=350){
      if(distanceR > distanceL ){
      
        SPEED_Right = 180;
        SPEED_Left = 175;
        color(124, 252, 0);         //LAWNGREEN
        digitalWrite(in3, HIGH);      // FORWARD    RIGHT
        digitalWrite(in4, HIGH);
        digitalWrite(in2, LOW);       // REVERS 
        digitalWrite(in1, LOW);        // RIGHT
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('350 LEFT Velocity range (R>L) = ');
        Serial.println(SPEED_Left);
        Serial.print('350 RIGHT Velocity range (R>L) = ');
        Serial.println(SPEED_Right);
        
      }else if(distanceL > distanceR){
        SPEED_Right = 175;
        SPEED_Left = 180;
        color(124, 252, 0);         //LAWNGREEN
        digitalWrite(in3, HIGH);
        digitalWrite(in4, HIGH);
        digitalWrite(in2, LOW);
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);

        Serial.print('350 LEFT Velocity range (R<L) = ');
        Serial.println(SPEED_Left);
        Serial.print('350 RIGHT Velocity range (R<L) = ');
        Serial.println(SPEED_Right);
        }
        else
        {

        SPEED_Right = 170;
        SPEED_Left = 170;
        color(124, 252, 0);         //LAWNGREEN
        digitalWrite(in3, HIGH);
        digitalWrite(in4, HIGH);
        digitalWrite(in2, LOW);
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('350 LEFT Velocity range (DR==DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('350 RIGHT Velocity range (DR==DL) = ');
        Serial.println(SPEED_Right);
      } 
      //------------------------------------------------------------------------

    }else if(distanceR >=200 && distanceL >=200){
      if(distanceR > distanceL ){
      
        SPEED_Right = 170;
        SPEED_Left = 165;

        color(255,255,0);           //YELLOW
        color(0, 255, 0);            // LIME
        digitalWrite(in3, HIGH);
        digitalWrite(in4, HIGH);
        digitalWrite(in2, LOW);
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);

        Serial.print('>=200 LEFT Velocity range (DR>DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('>=200 RIGHT Velocity range (DR>DL) = ');
        Serial.println(SPEED_Right);
        
      }else if(distanceL > distanceR){
        SPEED_Right = 165;
        SPEED_Left = 170;
      
        color(255,255,0);           //YELLOW
        color(0, 255, 0);           //LIME
        digitalWrite(in3, HIGH);
        digitalWrite(in4, HIGH);
        digitalWrite(in2, LOW);
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('>=200 LEFT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('>=200 RIGHT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Right);
        }else{
        SPEED_Right = 160;
        SPEED_Left = 160;
       
        color(0, 255, 0);         // LIME
        digitalWrite(in3, HIGH);
        digitalWrite(in4, HIGH);
        digitalWrite(in2, LOW);
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('>=200 LEFT Velocity range (R==L) = ');
        Serial.println(SPEED_Left);
        Serial.print('>=200 RIGHT Velocity range (R==L) =');
        Serial.println(SPEED_Right);
      }
    }
    //------------------------------------------------------------------------

    else if(distanceR>130 && distanceL >130){
      if(distanceR > distanceL){
        SPEED_Right = 150;
        SPEED_Left = 145;

        color(0, 128, 0);         //GREEN
        color(255,255,0);         //YELLOW
        digitalWrite(in3, HIGH); // FORWARD RIGHT
        digitalWrite(in4,HIGH); //  FORWARD LEFT
        digitalWrite(in2, LOW);  // GOES REVERS LEFT
        digitalWrite(in1, LOW); // GOES REVERS RIGHT
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);

        Serial.print('100 LEFT Velocity range (DR>DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('100 RIGHT Velocity range (DR>DL) = ');
        Serial.println(SPEED_Right);
      }else if(distanceL > distanceR){
        SPEED_Right = 145;
        SPEED_Left = 150;
        color(0, 128, 0);         //GREEN
        color(255,255,0);         //YELLOW
        digitalWrite(in3, HIGH);
        digitalWrite(in4, HIGH);
        digitalWrite(in2, LOW); // REVERS
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        
        Serial.print('100 LEFT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('100 RIGHT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Right);
        }
      else{
        SPEED_Right = 140;
        SPEED_Left = 140;
        color(255, 215, 0);         //GOLD    
        digitalWrite(in3, HIGH);
        digitalWrite(in4, HIGH); // GOES LEFT
        digitalWrite(in2, LOW);
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('100 LEFT Velocity range (DR==DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('100 RIGHT Velocity range (DR>==DL) = ');
        Serial.println(SPEED_Right);
      }
      //------------------------------------------------------------------------

    }else if(distanceR>100 && distanceL >100){
      if(distanceR > distanceL){
        SPEED_Right = 130;
        SPEED_Left = 125;
        color(255,0,0);         //RED
        color(255,255,0);       // YELLOW
        digitalWrite(in3, HIGH);     // GOES FORWARD RIGHT
        digitalWrite(in4, HIGH);      // FORWARD LEFT
        digitalWrite(in2, LOW);      // REVERS LEFT 
        digitalWrite(in1, LOW);     // GOES REVERS RIGHT
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('30 LEFT Velocity range (DR>DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('30 RIGHT Velocity range (DR>DL) = ');
        Serial.println(SPEED_Right);

      }else if(distanceL > distanceR){
        SPEED_Right = 125;
        SPEED_Left = 130;
        color(255,0,0);         //RED
        color(255,255,0);       // YELLOW
        digitalWrite(in3, HIGH);
        digitalWrite(in4, HIGH);
        digitalWrite(in2, LOW);
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('30 LEFT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('30 RIGHT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Right);
        }
      else{
        SPEED_Right = 120;
        SPEED_Left = 120;
        color(128, 0, 0);         //Maroon
        digitalWrite(in3, HIGH);
        digitalWrite(in4, HIGH);
        digitalWrite(in2, LOW);
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('30 LEFT Velocity range (DR==DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('30 RIGHT Velocity range (DR==DL) = ');
        Serial.println(SPEED_Right);
      }
      //------------------------------------------------------------------------

    }else if(distanceR >70&& distanceL  >70){
      if(distanceR > distanceL ){
        SPEED_Right = 120;
        SPEED_Left = 115;
        color(255,0,0);         //RED
        color(255,255,0);       // YELLOW
        digitalWrite(in3, HIGH);  // FORWARD RIGHT / svinger mot venstre
        digitalWrite(in4, HIGH);     // FORWARD LEFT
        digitalWrite(in2, LOW);  // REVERS LEFT
        digitalWrite(in1, LOW);   // REVERS RIGHT
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('30 LEFT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('30 RIGHT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Right);
    }else if(distanceL > distanceR){
        SPEED_Right = 115;
        SPEED_Left = 120;
        color(255,0,0);         //RED
        color(255,255,0);       // YELLOW
        digitalWrite(in3, HIGH);   // FORWARD RIGHT
        digitalWrite(in4, HIGH); // NÅR DEN HIGH vil vinge mot høyre
        //delay(500);
        digitalWrite(in2, LOW);
        digitalWrite(in1, LOW); // REVERS RIGHT
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('30 LEFT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('30 RIGHT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Right);
    }else{
        SPEED_Right = 120;
        SPEED_Left = 120;
        color(255,0,0);         //RED
        color(255,255,0);       // YELLOW
        digitalWrite(in3, HIGH);
        digitalWrite(in4, HIGH);
        digitalWrite(in2, LOW);
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        analogWrite(ena1, SPEED_Right);
        Serial.print('30 LEFT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('30 RIGHT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Right);
    }
    //------------------------------------------------------------------------

    }else{ 
       
        if(distanceR < 70 || distanceL < 70 && distanceB>=4 && distanceB<350){
          if(distanceR > distanceL){
            
        SPEED_Right = 180;
        SPEED_Left = 250;
        color(255,0,0);         //RED
        color(255,255,0);       // YELLOW
        digitalWrite(in2, HIGH);   // LEFt REVERS
        digitalWrite(in1, LOW); // RIGHT REVERS
        analogWrite(ena1, SPEED_Right);
        //delay(100);
        digitalWrite(in3, HIGH);   // RIGHT Forward
        digitalWrite(in4, LOW); // NÅR DEN HIGH vil vinge mot høyre
        analogWrite(ena,  SPEED_Left );
        //delay(500);
        delay(100);

        Serial.print('30 RIGHT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Right);
        Serial.print('30 LEFT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Left);
          }else if(distanceL > distanceR){
        SPEED_Right = 250;
        SPEED_Left = 180;
        color(255,0,0);         //RED
        color(255,255,0);       // YELLOW
        digitalWrite(in2, LOW); // LEFt REVERS      // LOW
        digitalWrite(in1, HIGH);
        analogWrite(ena,  SPEED_Left );
        digitalWrite(in3, LOW);   //
        digitalWrite(in4, HIGH); // NÅR DEN HIGH vil vinge mot høyre
        analogWrite(ena1, SPEED_Right);
       // delay(500);
        delay(100);

        Serial.print('30 LEFT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('30 RIGHT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Right);
    }else{
        SPEED_Right = 130;
        SPEED_Left = 130;
        color(255,0,0);         //RED
        color(255,255,0);       // YELLOW
        digitalWrite(in2, HIGH); // LEFt REVERS
        digitalWrite(in1, HIGH);
        analogWrite(ena,  SPEED_Left );
        digitalWrite(in3, LOW);   //
        digitalWrite(in4, LOW); // NÅR DEN ER HIGH vil vinge mot høyre
        analogWrite(ena1, SPEED_Right);
        Serial.print('30 LEFT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Left);
        Serial.print('30 RIGHT Velocity range (DR<DL) = ');
        Serial.println(SPEED_Right);
    }
    
    }
    }}}
  //------------------------------------------------------------------------



void loop(){
  // check for new cards
  if(! mfrc522.PICC_IsNewCardPresent())
    return;
    // Read the card
  if(! mfrc522.PICC_ReadCardSerial())
    return;

  byte_array(mfrc522.uid.uidByte, mfrc522.uid.size);

  if(read_rfid ==start_tank){
    READ_CARD_AND_START_TANK();
    Serial.println(start_tank);
  }else if(read_rfid !=start_tank){
//----------------------------------
// Front Right
   digitalWrite(trigR, LOW);
// Front LEFT
  
  digitalWrite(trigL, LOW);  
// REVERS
  digitalWrite(trigB, LOW);
//----------------------------------

      color(0,0,255);
        SPEED_Right = 0;
        SPEED_Left = 0;
        digitalWrite(in2, LOW); // LEFt REVERS
        digitalWrite(in1, LOW);
        analogWrite(ena,  SPEED_Left );
        digitalWrite(in3, LOW);   //
        digitalWrite(in4, LOW); // NÅR DEN ER HIGH vil vinge mot høyre
        analogWrite(ena1, SPEED_Right);

  }
}
 