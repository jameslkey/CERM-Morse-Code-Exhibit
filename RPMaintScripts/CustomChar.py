# -*- coding: utf-8 -*-
import time

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

lcd.create_char(0, [15, 29, 29, 29, 13, 5, 5, 5])  # Pilcrow
lcd.create_char(1, [0, 27, 9, 9, 0, 0, 0, 0])  # Left Double Quote
lcd.create_char(2, [0, 27, 18, 18, 0, 0, 0, 0])  # Right Double Quote

lcd.clear()
lcd.set_backlight(1)
lcd.message('\x00 \x01 \x02')
time.sleep(3)
lcd.clear()
lcd.set_color(1, 0, 0)
lcd.message('.,? !\'/ ()& :;-')
time.sleep(3)
lcd.clear()
lcd.set_color(0, 1, 0)
lcd.message('0123456789')
time.sleep(3)
lcd.clear()
lcd.set_color(0, 1, 1)
lcd.message('ABCDEFG')
time.sleep(3)
lcd.clear()
lcd.message('HIJKLMNO')
time.sleep(3)
lcd.home()
lcd.message('PQRSTUVWXYZ')
time.sleep(3)
lcd.clear()
lcd.set_backlight(0)
lcd.enable_display(False)
