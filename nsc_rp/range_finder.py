import serial
import RPi.GPIO as GPIO
import time
import threading
from config_manager import *
from config_value import ConfigValue

class RangeFinder():
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyAMA0", 115200)
        GPIO.setmode(GPIO.BCM)
        self.curtime = 0
        self.out_valve_start_time = None
        self.cur_spray_on = None

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

                if distance < (float(ConfigManager().get_value("detect_distance_meter")) * 100) :
                    self.curtime = time.time()
                    self.spray_on()
                else:
                    if time.time() - self.curtime > float(ConfigManager().get_value("detect_spray_duration_sec")) :
                        print("Here Here Here===")
                        self.spray_off()
                    else:
                        self.spray_on()

                self.ser.reset_input_buffer()

                return distance;

    def spray_on(self):
        self.cur_spray_on = True
        GPIO.output(ConfigValue.SPRAY_WPI_NUM, True)
        GPIO.output(ConfigValue.VALVE_WPI_NUM, False)

    def spray_off(self):
        if self.cur_spray_on:
            self.cur_spray_on = False
            GPIO.output(ConfigValue.SPRAY_WPI_NUM, False)
            self.out_valve_start_time = time.time()
            self.on_out_valve()            

    def on_out_valve(self):
        if time.time() - self.out_valve_start_time < ConfigValue.VALVE_ON_TIME:
            GPIO.output(ConfigValue.VALVE_WPI_NUM, True)
        else:
            GPIO.output(ConfigValue.VALVE_WPI_NUM, False)
            return True
        threading.Timer(0.1, self.on_out_valve).start()