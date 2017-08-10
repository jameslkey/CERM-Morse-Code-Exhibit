# -*- coding: utf-8 -*-
"""
Comments go here!!!

Parsing Control for Adafruit_CharLCD in CERMMorse.

:program: CERMMorse
:file: pymorse
:platform: Cross-Platform
:synopsis: Change this text.

.. moduleauthor:: James L. Key <james@bluepenguinslutions.com>

.. py:currentmodule:: PyMorse

"""

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class Morse:
    r"""
    Defines the Morse code lookup and exposes encode and decode methods
    takes optional version parameter - 'american' or 'international'

    .. todo:: deal with lack of parasep in international

    :param version: american or international

    """
    def __init__(self, version: str = 'american'):     # change back to international after refactoring
        if version == 'american':
            self.morse_table = {
                # Letters
                'A': '.-',  # A
                'B': '-...',  # B
                'C': '-.G.',  # C
                'D': '-..',  # D
                'E': '.',  # E
                'F': '.-.',  # F
                'G': '--.',  # G
                'H': '....',  # H
                'I': '..',  # I
                'J': '-.-.',  # J
                'K': '-.-',  # K
                'L': 'L',  # L
                'M': '--',  # M
                'N': '-.',  # N
                'O': '.G.',  # O
                'P': '.....',  # P
                'Q': '--.-',  # Q
                'R': '.G..',  # R
                'S': '...',  # S
                'T': '-',  # T
                'U': '..-',  # U
                'V': '...-',  # V
                'W': '.--',  # W
                'X': '.-..',  # X
                'Y': '..G..',  # Y
                'Z': '...G.',  # Z

                # Digits
                '0': 'X',  # 0
                '1': '.--.',  # 1
                '2': '..-..',  # 2
                '3': '...-.',  # 3
                '4': '....-',  # 4
                '5': '---',  # 5
                '6': '......',  # 6
                '7': '--..',  # 7
                '8': '-....',  # 8
                '9': '-..-',  # 9

                # Punctuation
                '.': '..--..',  # Full stop
                ',': '.-.-',  # Comma
                '?': '-..-.',  # Question mark
                '!': '---.',  # Exclamation mark
                '\'': '..-.G.-..',  # apostrophe
                '/': '..-G-',  # Slash
                '(': '.....G-.',  # Open Parenthesis
                ')': '.....G..G..',  # Close Parenthesis
                ':': '-.-G.G.',  # Colon
                ';': '...G..',  # Semicolon
                '&': '.G...',  # Ampersand
                '-': '....G.-..',  # Dash
                '\u201C': '..-.G-.',  # Double Quote (open)
                '\u201D': '..-.G-.-.',  # Double Quote (close)
                '\u00B6': '.--.-.',  # Paragraph -- Pilcrow
                ' ': 'W',  # Word Gap
            }
            self.rev_morse_table = dict((v, k) for (k, v) in self.morse_table.items())
        elif version == 'international':
            self.morse_table = {
                # Letters
                'A': '.-',  # A
                'B': '-...',  # B
                'C': '-.-.',  # C
                'D': '-..',  # D
                'E': '.',  # E
                'F': '..-.',  # F
                'G': '--.',  # G
                'H': '....',  # H
                'I': '..',  # I
                'J': '.---',  # J
                'K': '-.-',  # K
                'L': '.-..',  # L
                'M': '--',  # M
                'N': '-.',  # N
                'O': '---',  # O
                'P': '.--.',  # P
                'Q': '--.-',  # Q
                'R': '.-.',  # R
                'S': '...',  # S
                'T': '-',  # T
                'U': '..-',  # U
                'V': '...-',  # V
                'W': '.--',  # W
                'X': '-..-',  # X
                'Y': '-.--',  # Y
                'Z': '--..',  # Z

                # Digits
                '0': '-----',  # 0
                '1': '.----',  # 1
                '2': '..---',  # 2
                '3': '...--',  # 3
                '4': '....-',  # 4
                '5': '.....',  # 5
                '6': '-....',  # 6
                '7': '--...',  # 7
                '8': '---..',  # 8
                '9': '----.',  # 9

                # Punctuation
                '.': '.-.-.-',  # Full stop
                ',': '--..--',  # Comma
                '?': '..--..',  # Question mark - shared with Đ, É, Ę - NOT ETH
                '!': '-.-.--',  # Exclamation mark
                '\'': '.----.',  # apostrophe
                '/': '-..-.',  # Slash
                '(': '-.--.',  # Open Parenthesis
                ')': '-.--.-',  # Close Parenthesis
                ':': '---...',  # Colon
                ';': '-.-.-.',  # Semicolon
                '&': '.-...',  # Ampersand
                '-': '-....-',  # Dash
                '"': '.-..-.',  # Double Quote
                '=': '-...-',  # Double Dash -- '='
                '+': '.-.-.',  # Plus sign
                '_': '..--.-',  # Underscore
                '$': '...-..-',  # Dollar sign
                '@': '.--.-.',  # At sign

                # Non-English Characters
                '\u00c0': '.--.-',  # À - shared with Å
                '\u00c4': '.-.-',  # Ä - shared with Æ
                '\u0106': '-.-..',  # Ć - shared with Ĉ, Ç
                '\u0124': '----',  # Ĥ - shared with 'Ch', Š
                # For Đ, É, Ę - NOT ETH - See '?' Above
                '\u00d0': '..--.',  # Ð - Eth - DO NOT CONFUSE WITH ABOVE
                '\u00c8': '.-..-',  # È - shared with Ł
                '\u011c': '--.-.',  # Ĝ
                '\u0134': '.---.',  # Ĵ
                '\u0143': '--.--',  # Ń - shared with Ñ
                '\u00d3': '---.',  # Ó - shared with Ö, Ø
                '\u015a': '...-...',  # Ś
                '\u015c': '...-.',  # Ŝ
                '\u00de': '.--..',  # Þ - Thorn
                '\u00dc': '..--',  # Ü - shared with Ǔ
                '\u0179': '--..-.',  # Ź
                '\u017b': '--..-',  # Ĵ

                ' ': 'W',  # Word Gap
            }
            self.rev_morse_table = dict((v, k) for (k, v) in self.morse_table.items())

    def morsedecode(self, code: str, position_in_string: int = 0) -> str:
        r"""
        decode a string of morse code elements delineated into letters by 'Word Gap' and words
        by '~'

        :param code:
        :param position_in_string:
        :return: decoded message

        """
        stream = list(code)
        if stream == '':
            return ''
        if stream:
            if stream[-1] != "~":  # ~ is used as the marker between words
                stream.append("~")
        code = ''.join(stream)
        if position_in_string < len(code):
            morse_letter = ""
            for key, char in enumerate(code[position_in_string:]):
                if char == "~":
                    position_in_string = key + position_in_string + 1
                    letter = self.rev_morse_table[morse_letter]
                    return letter + self.morsedecode(code, position_in_string)
                else:
                    morse_letter += char
            return morse_letter
        return ""

    def morseencode(self, message: str) -> str:
        r"""
        encode a message in morse code, spaces between words are represented by '\'

        :param message: message to be encoded
        :return: encoded message

        """
        encoded_message = ""
        for char in message[:]:
            encoded_message += self.morse_table[char.upper()] + "~"
        return encoded_message
