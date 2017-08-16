# -*- coding: utf-8 -*-
"""
Comments go here!!!

:module: LcdScroll
:program: CERM20
:file: lcdscroll
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: LcdScroll

"""

import os
if os.name == 'nt':
    import Waxfruit_CharLCD as Adafruit_CharLCDPlate
else:
    import Adafruit_CharLCD
    from Adafruit_CharLCD import Adafruit_CharLCDPlate  # pylint: disable=F0401


class LcdScroll:
    # pylint: disable=R0902
    r"""
    Parsing Control for Adafruit_CharLCD in CERMMorse

    This class implements a set of methods to scroll messages upward on a LCD display.
    The limits are adjustable to different lengths and rows depending on hardware, It parses
    the message into words and check if there is enough space left on the screen and if not
    pushes the display up then prints the word.
    Also a method to move the cursor from letter to letter like follow the bouncing ball
    in a sing along.

    .. todo:: remove this fake assignment of Lcd.Adafruit...

    :param lcd: Adafruit CharLCD object (req.)

    """

    def __init__(self, lcd, cols: int=16, lines: int=2, cursor: bool=False):
        #: Adafruit CharLCD Object
        """if not isinstance(lcd, Adafruit_CharLCD.Adafruit_CharLCD):
            self.lcd = Adafruit_CharLCD.Adafruit_CharLCDPlate(cols=cols, lines=lines)"""

        #: Tuple containing display and init to common values
        self._display_size = [cols, lines]
        #: Internal Message to send
        self._message = ''
        #: Internal dictionary of special characters
        self._special_characters = {' ': None}
        if not isinstance(self.special_characters, dict):
            raise LcdScrollEx('special_characters need to be a dictionary object')
        self._screen_buffer = []
        self._line_buffer = ''
        self._word_buffer = ''
        self._remaining_line_buffer, _ = self.display_size
        #: Internal "bouncing ball" cursor switch
        self._cursor_enabled = cursor
        #: current position of cursor
        self._cursor_position = 0

    @property
    def message(self) -> str:
        r"""
        Property: Message buffer to be processed and sent

        :getter: Get LcdScroll.message property
        :setter (String): Set LcdScroll.message property

        Examples::

        my_message = LcdScroll.message()

        LcdScroll.message('This is a message')

        """
        return self._message

    @message.setter
    def message(self, message: str):
        r"""
        Set current message into buffer to be sent

        """
        self._message = message

    @property
    def special_characters(self) -> dict:
        r"""
        Property: List of special characters that need special handling

        :getter: Get LcdScroll.special_characters property
        :setter (Dictionary): Set LcdScroll.special_characters property

        Example::

            spec_char = LcdScroll.special_characters()

            LcdScroll.special_characters({'\u00B': '\x00', }

        """
        return self._special_characters

    @special_characters.setter
    def special_characters(self, special_characters: dict):
        """
        Set special character list

        """
        self._special_characters = special_characters

    @property
    def display_size(self) -> tuple:
        r"""
        Property: LCD display area columns, rows

        :getter: Get ScrollLCD.display_size property
        :setter Int, Int: Set the ScrollLcd.display_size property

        Examples::

            columns, rows = LcdScroll.display_size()

            LcdScroll.display_size(columns=16, rows=2)

        """
        return self._display_size[0], self._display_size[1]

    @property
    def columns(self) -> int:
        r"""

        :return int:

        """
        return self._display_size[0]

    @columns.setter
    def columns(self, columns: int = 16):
        r"""
        Set display size

        """
        if columns <= 0:
            raise LcdScrollEx('Error display_size must be positive integers greater than zero')
        self._display_size[0] = columns

    @property
    def lines(self) -> int:
        r"""

        :return int:

        """
        return self._display_size[1]

    @lines.setter
    def lines(self, lines: int = 1):
        r"""
        Set display size

        """
        if lines <= 0:
            raise LcdScrollEx('Error display_size must be positive integers greater than zero')
        self._display_size[1] = lines

    @property
    def display_cursor(self) -> bool:
        """
        Property: Set to enable of disable "Bouncing Ball" cursor during display

        :getter: Get ScrollLCD.display_cursor property
        :setter (Bool): Set the ScrollLcd.display_size property

        Returns:
           Bool: Option state

        Examples::

            if(LcdScroll.display_cursor()):
                do_something()

            LcdScroll.display_cursor(True)

        """
        return self._cursor_enabled

    @display_cursor.setter
    def display_cursor(self, enabled: bool = True):
        """
        Set true if "bouncing ball" cursor is desired

        """
        self._cursor_enabled = enabled

    def trigger_cursor(self, position: int):
        """
        Trigger the cursor movement or set to custom location.
        Second line.

        :param position:

        """
        self._cursor_position = position

    def trigger_letter(self, index: int):
        """
        Trigger the display of next letter or letter at index (0 based)

        :param index:
        :return:

        """
        pass

    def send_character(self, char: str):
        """
        Sends one character to the display. Primarily used by bouncing ball option.
        To be overridden by derived classes to add functionality.

        :param char:


        """
        self.lcd.message(char)

    def send_word(self, word: str):
        """
        Sends one word to the display.
        To be overridden by derived classes to add functionality.

        :param word:


        """
        self.lcd.message(word)

    def send_message(self):
        """
        Method to initiate sending

        .. todo:: Not end of string in message?

        """
        '''
        Order of events:

        --get message
        --break into words
        --calculate if there is room on the line if not new line

        if Bouncing Ball
        place word on line
        move visible cursor to first letter of word
        send corresponding morse character
        iterate though word one letter at a time
        --if not Bouncing Ball
        --send word one character at a time to LCD

        '''
        # set initial state
        columns, rows = self.display_size
        self.lcd.clear()
        self.lcd.show_cursor(False)
        self._line_buffer = 0
        self._cursor_position = 0
        for row in range(0, rows - 1):
            self._screen_buffer[row] = ''

        def scroll_up():
            screen_buffer = []
            if rows > 0:
                for row in range(1, rows - 1):
                    screen_buffer[row - 1] = self._screen_buffer[row]
                for row in range(0, rows - 1):
                    self.lcd.set_cursor(0, row)
                    self.lcd.message(self._screen_buffer[row])
                self._screen_buffer = screen_buffer

        # break into words
        local_message = self.message.split(' ')

        while True:
            try:
                for word in local_message:  # feed one at a time to display
                    if len(str(self._line_buffer)) is 0:  # Move cursor to Bottom line
                        self.lcd.set_cursor(0, rows - 1)
                    # calculate if there is room on the line if not move text up
                    if len(word) > self._remaining_line_buffer:
                        self.lcd.clear()
                        scroll_up()
                        self._remaining_line_buffer = columns
                        # === logic sounds good until here
                    if self.display_cursor:
                        while True:
                            # iterate number of letters?
                            # cursor 0 - col-1
                            # calc word length
                            self.send_word(word)  # display word
                            # set cursor pos to current - word length
                            # make cursor visible?
                            # iterate letters of word
                            # play char
                            # move cursor
                            # if iteration var = word length: break | or try: except:?
                    else:
                        while True:
                            # while True iterate number of letters
                            for char in word.split():
                                # display letter
                                self.send_character(char)



                    """if word:  # catch null characters
                        self.lcd.message(self._screen_buffer[0])
                    self._screen_buffer[0] = ''"""
            except IndexError:
                break


class LcdScrollEx(Exception):
    """
    Internal Exception for Scroll Class
    """
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
