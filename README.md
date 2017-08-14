# Connecticut Eastern Railroad Museum's Dynamic Morse Code Exhibit
http://www.cteastrrmuseum.org/

This is the software for the Connecticut Eastern Railroad Museum's Dynamic Morse Code Exhibit.
 It runs on a Raspberry Pi (currently a Pi Zero but should on any Pi) using:
 * a PIR Motion detector
 * an Adafruit RGB LCD Plate
 * a relay driver board 
### The idea is to emulate a morse session, sounding on the station's morse responder, when a visitor moves into the station activating the PIR Motion detector.
 It is written in Python 3.4 and tries to maintain the PEP-8 standards.

#### This project uses *American Morse* code ***NOT** International* Morse Code, it can be modified without too many issues.
There are more options in the works:
* a wxPython based workorder and config editor
* choice of Morse varients
* possibly a morse interpreter from a GPIO connected Key
* integrated menu, using the LCD Plate's push Buttons


