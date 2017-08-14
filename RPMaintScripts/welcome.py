import time

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()
lcd_columns = 16
lcd.autoscroll(False)
lcd.show_cursor(False)
lcd.set_color(0, 1, 0)


def welcome():
    lcd.set_color(0, 1, 0)
    lcd.message(" Welcome to the ")
    lcd.set_cursor(0, 1)
    lcd.message("  Connecticut   ")
    time.sleep(3)
    lcd.set_cursor(0, 0)
    lcd.message("Eastern Railroad")
    lcd.set_cursor(0, 1)
    lcd.message("     Museum     ")
    time.sleep(10)
    lcd.set_backlight(0)
    lcd.clear()


welcome()
