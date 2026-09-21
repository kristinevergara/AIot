from machine import Pin
import utime

# Built-in red LED
led = Pin(13, Pin.OUT)
led.value(0)

# Timing (ms). Per the lab: dots blink at ~2x the speed of dashes,
# so a dash lasts twice as long as a dot.
DOT = 200
DASH = 2 * DOT
SYMBOL_GAP = DOT        # off-time between dots/dashes within a letter
LETTER_GAP = 3 * DOT    # off-time between letters
MESSAGE_GAP = 7 * DOT   # off-time before the message repeats

MORSE = {
    "S": "...",
    "O": "---",
}


def blink(duration):
    led.value(1)
    utime.sleep_ms(duration)
    led.value(0)


def send_letter(letter):
    for symbol in MORSE[letter]:
        blink(DOT if symbol == "." else DASH)
        utime.sleep_ms(SYMBOL_GAP)


def send_message(message):
    for letter in message:
        send_letter(letter)
        utime.sleep_ms(LETTER_GAP - SYMBOL_GAP)  # symbol gap already elapsed


while True:
    send_message("SOS")
    utime.sleep_ms(MESSAGE_GAP)
