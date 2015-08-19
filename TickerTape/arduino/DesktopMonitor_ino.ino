/*
This program was made by Victor Uribe vuribe1221@gmail.com and is provided free for use how you choose.

This is (obviously) an open source project share and modify to your hearts content! happy hacking. 
*/

#include <MicroView.h>

MicroViewWidget *vWidget1, *vWidget2;

String input = "";  // the message sent from the computer over to the microview

void setup() // this only runs once
{
	Serial.begin(9600);	// open the serial port on the arduino
	uView.begin();		// start the screen on the Microview
	uView.clear(PAGE);  // clear the screen in case anything was being displayed
  uView.print("init..");
	uView.display();	// show the newly made sliders
	Serial.println("READY!"); // tell user when the device is ready to recieve data, this will only show up if the serial port
	// is expecting a packet, as in the arduino IDE or codebender
}

void readSerial() // this is where the input from the serial port is initially processed
{
	if (Serial.available())
	{
		delay(50);
		while(Serial.available() > 0)
		{
      input = String(Serial.readStringUntil('\n'));
		}

	}
}


void loop()
{

readSerial();
uView.setCursor(0,0);
//if(strcmp(input,"0") == 0)
if (input == "0")
{
uView.clear(PAGE);
}
uView.print(input);
uView.display();
Serial.println(input); 
//delay(700);
}
