beaglebone_userled
==================

A python module to control the user LEDs 0 to 3 on a beaglebone black.

LED
---
There are four LEDS onboard that you can control on the beaglebone black. These are labeled USR0, USR1, USR2 and USR3 and you can find time next to the ethernet port. By default USR0 shows the system heartbeat and another LED blinks when the SD card is accesed. 

How to
-----
You can run the module as stand alone (as root) where the LEDs are controlled in the mainfunction(). Nothing spectaculaer here: it demos the basic functionality.

Or import this module in your own project and use the user leds for status updates, debugging or user interaction. Here is an example

```
import beaglebone_userled.pythonled as pythonled

user0 = pythonled(0)
user0.ledON()
```

Make sure the package is in the python searchpath and you run the script as root.

Why
---
Controlling the LEDs is like the `Hello World` program for the beaglebone. [Adafruit](http://adafruit.com) made a nice python library to control the GPIO, UART, PWM, etc, but I couldn't find something to control the onboard LEDS (named USR0, USR1, USR2 and USR3).
