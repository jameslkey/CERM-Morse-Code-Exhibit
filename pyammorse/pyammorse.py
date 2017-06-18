# coding=utf-8
"""
CERMMorse : pyammorse
5/12/2017 : 3:46 PM
Author : James L. Key
"""
# todo: write comments!!!

__author__ = 'James L. Key'
__project__ = 'CERMMorse'


class Morse:
    #: This should show up
    def __init__(self):
        self.amMorseTable = {
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

        self.revamMorseTable = dict((v, k) for (k, v) in self.amMorseTable.items())

    def morsedecode(self, code, position_in_string=0):
        stream = list(code)
        if stream == '':
            return ""
        if stream:  #catch fencepost error
            if stream[-1] != "~":
                stream.append("~")
        code = ''.join(stream)
        if position_in_string < len(code):
            morse_letter = ""

            for key, char in enumerate(code[position_in_string:]):

                if char == "~":
                    position_in_string = key + position_in_string + 1
                    letter = self.revamMorseTable[morse_letter]
                    return letter + self.morsedecode(code, position_in_string)

                else:
                    morse_letter += char
            return morse_letter
        else:
            return ""

    # encode a message in morse code, spaces between words are represented by '~'
    def morseencode(self, message):
        encoded_message = ""
        for char in message[:]:
            encoded_message += self.amMorseTable[char.upper()] + "~"

        return encoded_message
