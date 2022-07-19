# Snake Game

## Setting up ESP8266
The whole program is written in Micropython for ESP8266 so before getting started you have to flash the ESP8266 to run micropython.
Here is the documentation to do that https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html
This video online could help you if you still have any doubts about how to do this https://www.youtube.com/watch?v=dY0QyILX8NA
if you cannot find the com port in your device when plugged in device manager download this software from silicon labs https://www.silabs.com/documents/public/software/CP210x_Universal_Windows_Driver.zip
if you have a issue to run the esptool.py command lines just use "python-m esptool" instead of the "esptool.py"
Install Thonny to make modifications or to push the code to the microcontroller 

This program is to run snake game in a 15x15 Matrix made with WS2812B (5M 300led) Led Strip.

The boot.py is to connect to the wifi change the Username and Password to your Username and Password

I also added background.py for generation of the matrix if you are doing for a matrix of different size.

