from os import system

class usr_led():
    '''
    Controls the USR LEDs on the BeagleBone Black.
    '''

    def __init__(self, num: int) -> None:
        '''
        Constructor method to initialize the class with a valid number.

        Arguments:
            num: LED number (0 to 3) on the BeagleBone Black to control.
        '''
        if not isinstance(num, int):
            raise ValueError(f'LED number "{num}" is not an integer.')
        elif num not in range(4):
            raise ValueError(f'LED number "{num}" is not supported. Use either 0, 1, 2, or 3.')

        self.num: int = num

    def on(self) -> None:
        '''
        Switch the LED on by setting the trigger to 'none' and the brightness to 'high'.
        '''

        system(f'echo none > sys/class/leds/beaglebone\:green\:usr{self.num}/trigger')
        system(f'echo 1 > /sys/class/leds/beaglebone\:green\:usr{self.num}/brightness')

    def off(self) -> None:
        '''
        Switch the LED off by setting the trigger to 'none' and the brightness to 'low'.
        '''

        system(f'echo none > /sys/class/leds/beaglebone\:green\:usr{self.num}/trigger')
        system(f'echo 0 > /sys/class/leds/beaglebone\:green\:usr{self.num}/brightness')

    def dimm(self) -> None:
        '''
        Set the brightness of the LED to 'low'.
        '''

        system(f'echo 0 > /sys/class/leds/beaglebone\:green\:usr{self.num}/brightness')

    def bright(self) -> None:
        '''
        Set the brightness of the LED to 'high'.
        '''

        system(f'echo 1 > /sys/class/leds/beaglebone\:green\:usr{self.num}/brightness')

    def heartbeat(self) -> None:
        '''
        Set the bright of the LED to 'high' and pulse the LED with a heartbeat pattern.
        '''

        system(f'echo 1 > /sys/class/leds/beaglebone\:green\:usr{self.num}/brightness')
        system(f'echo heartbeat > /sys/class/leds/beaglebone\:green\:usr{self.num}/trigger')

    def times(self, delay_on: int, delay_off: int) -> None:
        '''
        Set the birghtness of the LED to 'high' and pulse the LED with 'delay_on' time
        and 'delay_off' time in milliseconds (ms).

        Arguments:
            delay_on: Number of milliseconds to keep LED on.
            delay_off: Number of milliseconds to keep LED off.
        '''

        if not isinstance(delay_on, int) or delay_on <= 0:
            raise ValueError(f'Delay value "{delay_on}" is invalid.')
        if not isinstance(delay_off, int) or delay_off <= 0:
            raise ValueError(f'Delay value "{delay_off}" is invalid.')

        system(f'echo 1 > /sys/class/leds/beaglebone\:green\:usr{self.num}/brightness')
        system(f'echo timer > /sys/class/leds/beaglebone\:green\:usr{self.num}/trigger')
        system(f'echo {delay_on} > /sys/class/leds/beaglebone\:green\:usr{self.num}/delay_on')
        system(f'echo {delay_off} > /sys/class/leds/beaglebone\:green\:usr{self.num}/delay_off')

    def transient(self, state: bool, period: int) -> None:
        '''
        Set a timer period in milliseconds (ms) and set the starting state (0 or 1).

        Arguments:
            state: Initial state for transient LED.
            period: Time for one period of the transient.
        '''

        if not isinstance(state, bool):
            raise ValueError('State variable must be a boolean.')
        if not isinstance(period, int) or period <= 0:
            raise ValueError(f'Period value "{period}" is invalid.')

        system(f'echo transient > /sys/class/leds/beaglebone\:green\:usr{self.num}/trigger')
        system(f'echo {state} > /sys/class/leds/beaglebone\:green\:usr{self.num}/state')
        system(f'echo {period} > /sys/class/leds/beaglebone\:green\:usr{self.num}/duration')
        system(f'echo 1 > /sys/class/leds/beaglebone\:green\:usr{self.num}/activate')
