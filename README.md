# iot-park-monitor
asset and weather monitor of a park using NXP's Rapid IoT kit and Raspberry pi as the gateway

Preparing the Software
There are few things needed to do for the software:

Raspbian
just follow this link to install the os

Python 2 or 3
Already built in for the raspbian

Pygatt and few of its components
$ pip install pygatt
$ pip install "pygatt[GATTTOOL]"
$ pip install pexpect
Pygatt is needed to read the advertisements data from the Rapid IoT kit using the ble connection

cloud4rpi
$ pip install cloud4rpi

This is needed to connect the data to the Cloud4rpi iot service
I already try various kind of online iot dashboard service such as ubidots, adafruit, thingspeak, etc. For this projects I am gonna use cloud4rpi because of its simplicity and easy to build dashboard system
Program the Rapid IoT Kit
The code and firmware that used for this projects are attached below. To reserve power I turn off the backlight and only send the data I need for the project. If you want clone the project just import the .atmo files attached above

