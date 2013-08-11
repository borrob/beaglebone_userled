import os

class pythonled(object):

    def __init__(self,led):
        if (led >= 0 and led <=3):
            self.lednumber = led
            #print 'Lednummer: %d' %(self.lednumber)
        else:
            print 'This lednumber is not supported. Use 0, 1, 2 or 3'

    def ledON(self):
        '''Switch the LED on
        by setting the trigger to 'none' and the brightness to 'high'. You need to sed the trigger
        to 'none' first or else it  would just brighten the LED and not make it static on''' 
       
        os.system('echo none > /sys/class/leds/beaglebone\:green\:usr%i/trigger' %(self.lednumber))
        os.system('echo 1 > /sys/class/leds/beaglebone\:green\:usr%i/brightness' %(self.lednumber))

    def ledOFF(self):
       '''Switch the LED off
       by setting the trigger to 'none' and the brightness to 'low'. You need to sed the trigger
       to 'none' first or else it  would just dimm the LED''' 
       
       os.system('echo none > /sys/class/leds/beaglebone\:green\:usr%i/trigger' %(self.lednumber))
       os.system('echo 0 > /sys/class/leds/beaglebone\:green\:usr%i/brightness' %(self.lednumber))

    def ledDIMM(self):
        '''Set the brightness low
           Use ledOFF to switch off the LED'''
       
        os.system('echo 0 > /sys/class/leds/beaglebone\:green\:usr%i/brightness' %(self.lednumber))

    def ledBRIGHT(self):
        '''Set the brightness high
           Use ledON to switch on the LED'''
       
        os.system('echo 1 > /sys/class/leds/beaglebone\:green\:usr%i/brightness' %(self.lednumber))

    def ledHEARTBEAT(self):
        '''Set the brightness high and pulse the LED with a hearbeat
           '''
       
        os.system('echo 1 > /sys/class/leds/beaglebone\:green\:usr%i/brightness' %(self.lednumber))
        os.system('echo heartbeat > /sys/class/leds/beaglebone\:green\:usr%i/trigger' %(self.lednumber))

    def ledTIMER(self,on,off):
        '''Set the brightness high and pulse the LED with ON time and OFF time (ms).
           '''
        os.system('echo 1 > /sys/class/leds/beaglebone\:green\:usr%i/brightness' %(self.lednumber))
        os.system('echo timer > /sys/class/leds/beaglebone\:green\:usr%i/trigger' %(self.lednumber))
        os.system('echo %i > /sys/class/leds/beaglebone\:green\:usr%i/delay_on' %(on,self.lednumber))
        os.system('echo %i > /sys/class/leds/beaglebone\:green\:usr%i/delay_off' %(off,self.lednumber))

    def ledTRANSIENT(self,state,timer):
        '''Set a timer
         Somehow the timerperiod (ms) is double what you would expect
         you can start in offstate or in onstate and the stat is toggled after the timerperiod.
         state: the starting state
           '''
        os.system('echo transient > /sys/class/leds/beaglebone\:green\:usr%i/trigger' %(self.lednumber))
        os.system('echo %i > /sys/class/leds/beaglebone\:green\:usr%i/state' %(state,self.lednumber))
        os.system('echo %d > /sys/class/leds/beaglebone\:green\:usr%i/duration' %(timer,self.lednumber))
        os.system('echo 1 > /sys/class/leds/beaglebone\:green\:usr%i/activate' %(self.lednumber))

def mainfunction():
    user0 = pythonled(0)
    user0.ledON()
    user1 = pythonled(1)
    user1.ledHEARTBEAT()
    user2 = pythonled(2)
    user2.ledTIMER(250,100)
    user3 = pythonled(3)
    user3.ledTRANSIENT(0,1000)

if __name__ == '__main__':
    mainfunction()
