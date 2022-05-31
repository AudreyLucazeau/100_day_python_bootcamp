from beep_sound import long_beep, short_beep, DURATION_BEEP
from morse_code import MORSE_CODE
import time

def code_message(message):
    morse_message = ""
    for letter in message:
        if letter == ' ':
            morse_message += " "
        else:
            try :
                morse_message += MORSE_CODE[letter]

            except ValueError:
                print("The character is not recognized")
    return morse_message


def read_message(morse_message):
    for mark in morse_message:
        time.sleep(DURATION_BEEP)
        if mark == '.':
            short_beep()
        elif mark == '-':
            long_beep()
        elif mark == ' ':
            time.sleep(2*DURATION_BEEP)
        else:
            print("impossible to transmit the signal")

