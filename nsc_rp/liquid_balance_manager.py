import time
import sys
# import RPi.GPIO as GPIO
# from hx711 import HX711
import random
import threading

class LiquidBalanceManager:

    def __init__(self, func):
        # liquid_balance_ratio = 100
        # liquid_balance_full_gram = 18000
        # liquid_balance_empty_gram = 1000
        # liquid_balance_recent_gram = 5000

        # referenceUnit = 1
        # hx = None

        # LiquidBalanceManager.hx = HX711(5, 6)
        # LiquidBalanceManager.hx.set_reading_format("MSB", "MSB")
        # LiquidBalanceManager.hx.set_reading_format("MSB", "MSB")
        # LiquidBalanceManager.hx.reset()
        # LiquidBalanceManager.hx.tare()
        print("Tare done! Add weight now...")
        t = threading.Thread(target=self.read_value(func))
        t.start()

    def read_value(self, func):
        # while True:
        #     try:
        #         # val = LiquidBalanceManager.hx.get_weight(5)
        #         # print(val)
        #         # LiquidBalanceManager.hx.power_down()
        #         # LiquidBalanceManager.hx.power_up()
        #         # time.sleep(0.1)
        #         val = random.randint(0, 100)
        #         print(str(val))
        #         func(val)

        #     except (KeyboardInterrupt, SystemExit):
        #         LiquidBalanceManager.cleanAndExit()

        #     time.sleep(1)
        while True:
            val = random.randint(0, 100)
            print(str(val))
            func(val)
            time.sleep(1)



    def cleanAndExit(self):
        print("Cleaning...")
        # GPIO.cleanup()
        print("Bye!")
        sys.exit()