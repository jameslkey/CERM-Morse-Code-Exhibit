# coding=utf-8
"""
CERMMorse : threadtest
5/26/2017 : 11:34 PM
Author : James L. Key
"""

import _thread
import os
import queue
import time

if os.name == 'nt':
    import Waxfruit_CharLCD as Lcd
    from Adafruit_CharLCD import RIGHT, UP, DOWN, LEFT, SELECT
else:
    import Adafruit_CharLCD as Lcd
    from Adafruit_CharLCD import RIGHT, UP, DOWN, LEFT, SELECT
__author__ = 'James L. Key'
__project__ = 'CERMMorse'

dataQueue = queue.Queue()
lcd = Lcd.Adafruit_CharLCDPlate()
buttons = (LEFT, RIGHT, UP, DOWN, SELECT)

lcd.create_char(0, [0, 0, 15, 29, 29, 13, 5, 5])  # Pilcrow
lcd.create_char(1, [0, 27, 9, 9, 0, 0, 0, 0])  # Left Double Quote
lcd.create_char(2, [0, 27, 18, 18, 0, 0, 0, 0])  # Right Double Quote
lcd.create_char(3, [0, 2, 6, 14, 6, 2, 0, 0])  # Left Arrow
lcd.create_char(4, [0, 8, 12, 14, 12, 8, 0, 0])  # Right Arrow
lcd.create_char(5, [0, 0, 4, 14, 31, 0, 0, 0])  # Up Arrow
lcd.create_char(6, [0, 0, 31, 14, 4, 0, 0, 0])  # Down Arrow
lcd.enable_display(1)


def producer(id):
    while True:
        for button in buttons:
            if lcd.is_pressed(button):
                if button is LEFT:
                    dataQueue.put('\x03')
                if button is RIGHT:
                    dataQueue.put('\x04')
                if button is UP:
                    dataQueue.put('\x05')
                if button is DOWN:
                    dataQueue.put('\x06')
                if button is SELECT:
                    dataQueue.put("SEL")


def consumer():
    while True:
        try:
            lcd.message('get')
            data = dataQueue.get(block=False)
            time.sleep(.5)
            lcd.clear()
        except queue.Empty:
            pass
        else:
            lcd.message('got => %s' % str(data))
            time.sleep(1)
            lcd.clear()
            data = ''
        time.sleep(1)
        lcd.clear()


def makethread():
    _thread.start_new_thread(producer, (1,))


if __name__ == '__main__':
    makethread()
    consumer()
