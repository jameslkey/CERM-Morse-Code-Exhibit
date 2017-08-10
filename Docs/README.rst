Connecticut Eastern Railroad Museum's Dynamic Morse Code Exhibit
================================================================

http://www.cteastrrmuseum.org/

| This is the software for the Connecticut Eastern Railroad Museum's
  Dynamic Morse Code Exhibit.
| It runs on a Raspberry Pi (currently a Pi Zero but should on any Pi)
  using:

-  a PIR Motion detector
-  an Adafruit RGB LCD Plate
-  a relay driver board

   .. rubric:: The idea is to emulate a morse session, sounding on the
      station's morse responder, when a visitor moves into the station
      activating the PIR Motion detector.
      :name: the-idea-is-to-emulate-a-morse-session-sounding-on-the-stations-morse-responder-when-a-visitor-moves-into-the-station-activating-the-pir-motion-detector.

   It is written in Python 3.4 and tries to maintain the PEP-8
   standards.

This project uses *American Morse* code by default it can be set for *International* Morse Code, it can be modified without too many issues.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are more options in the works:

-  a wxPython based workorder and config editor
-  possibly a morse interpreter from a GPIO connected Key
-  integrated menu, using the LCD Plate's push Buttons
