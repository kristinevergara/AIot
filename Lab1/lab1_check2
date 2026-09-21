from machine import Pin
import utime
import neopixel

# NeoPixel needs its power-enable pin driven high
pwr = Pin(2, Pin.OUT)
pwr.value(1)

# LED 1: built-in red LED
led1 = Pin(13, Pin.OUT)
led1.value(0)

# LED 2: built-in NeoPixel
np_led = neopixel.NeoPixel(Pin(0, Pin.OUT), 1)
np_led[0] = (0, 0, 0)
np_led.write()

# Toggle intervals (ms)
LED1_INTERVAL = 100
LED2_INTERVAL = 500

ON_COLOR = (50, 50, 50)   # white, dimmed so it isn't blinding
OFF_COLOR = (0, 0, 0)

# Polling loop: no sleep(), no Timer, no IRQ. Each pass we check the
# clock and toggle whichever LED is due.
now = utime.ticks_ms()
next1 = utime.ticks_add(now, LED1_INTERVAL)
next2 = utime.ticks_add(now, LED2_INTERVAL)

while True:
    now = utime.ticks_ms()

    if utime.ticks_diff(now, next1) >= 0:
        led1.value(not led1.value())
        next1 = utime.ticks_add(next1, LED1_INTERVAL)

    if utime.ticks_diff(now, next2) >= 0:
        np_led[0] = OFF_COLOR if np_led[0] != OFF_COLOR else ON_COLOR
        np_led.write()
        next2 = utime.ticks_add(next2, LED2_INTERVAL)
