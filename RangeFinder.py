import serial
import odroid_wiringpi as wpi
import time

class RangeFinder():
    def __init__(self, controller):
        self.ser = serial.Serial("/dev/ttyS1", 115200)
        wpi.wiringPiSetup()
        wpi.pinMode(4, 1)
        self.curtime = 0
        self.controller = controller

        try:
            if self.ser.isOpen() == False:
                self.ser.open()
        except KeyboardInterrupt(): # ctrl + c in terminal.
            if self.ser != None:
                self.ser.close()
                print("program interrupted by the user")

    def read(self):
        counter = self.ser.in_waiting # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = self.ser.read(9)
            self.ser.reset_input_buffer()

            # this portion is for python3
            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59:
                # multiplied by 256, because the binary data is shifted by 8 to the left (equivalent to "<< 8").
                # Dist_L, could simply be added resulting in 16-bit data of Dist_Total.
                distance = bytes_serial[2] + bytes_serial[3]*256
                strength = bytes_serial[4] + bytes_serial[5]*256
                temperature = bytes_serial[6] + bytes_serial[7]*256
                temperature = (temperature/8) - 256
                print("Distance:"+ str(distance))
                print("Strength:" + str(strength))

                if distance < (self.controller.distanceModeDetectDistance * 100) :
                    self.curtime = time.time()
                    wpi.digitalWrite(4, 1)
                else:
                    if time.time() - self.curtime > self.controller.distanceModeSprayTime :
                        wpi.digitalWrite(4, 0)

                if temperature != 0:
                    print("Temperature:" + str(temperature))

                self.ser.reset_input_buffer()

                return distance;