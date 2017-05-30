import time

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)
lcd = LCD.Adafruit_CharLCDPlate()
lcd_columns = 16
lcd.autoscroll(False)
lcd.show_cursor(False)
# lcd.set_cursor(16, 0)
lcd.set_color(1, 0, 0)
time.sleep(.1)
lcd.set_color(0, 1, 0)
time.sleep(.1)
lcd.set_color(1, 0, 0)
time.sleep(.1)
lcd.set_color(0, 1, 0)
time.sleep(.1)
lcd.set_color(1, 0, 0)
time.sleep(.1)
lcd.set_color(0, 1, 0)
time.sleep(.1)


def click():
    GPIO.output(26, GPIO.LOW)
    print("start on")
    time.sleep(.25)
    print("end on")
    GPIO.output(26, GPIO.HIGH)


def scroll(lcd, text, pause1=False, pause2=False, rep=False):
    # Edit following lines to change timing defaults. Remember you can decide them when you call the function.
    PAUSE_NEXT = 2
    PAUSE_REP = 2
    REPETITIONS = 1

    if pause1: PAUSE_NEXT = pause1
    if pause2: PAUSE_REP = pause2
    if rep: REPETITIONS = rep

    n = 16
    rows = [text[i:i + n] for i in range(0, len(text), n)]
    n_rows = len(rows)
    for i in range(REPETITIONS):
        for x in range(n_rows):
            lcd.home()
            lcd.clear()
            nxt = x + 1
            lcd.message(rows[x] + "\n")
            if nxt == n_rows:
                time.sleep(2)

                break
            else:
                lcd.message(rows[nxt])
                time.sleep(PAUSE_REP)

    lcd.clear()


def wait_for_motion():
    try:
        while True:
            i = GPIO.input(20)
            if i == 1:
                print("click")
                break
    except KeyboardInterrupt:
        pass


message = 'Welcome to CT Eastern Railroad Museum Morse Code Example\n More words here to see more scolling!'
scroll(lcd, message)
lcd.set_backlight(0)
lcd.clear()

try:
    while True:
        wait_for_motion()
        lcd.clear()
        lcd.set_backlight(1)
        lcd.set_cursor(16, 1)
        for x in range(3):
            for i in range(10):
                click()
                lcd.message(str(i) + ' ')
                lcd.move_left()
        lcd.set_backlight(0)
except KeyboardInterrupt:
    lcd.set_backlight(0)
    lcd.clear()
    GPIO.output(26, GPIO.HIGH)
