import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)
lcd = LCD.Adafruit_CharLCDPlate()

GPIO.output(26, GPIO.HIGH)
lcd.clear()

lcd.set_backlight(0)
