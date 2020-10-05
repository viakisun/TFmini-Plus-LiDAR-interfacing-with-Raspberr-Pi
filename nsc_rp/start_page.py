#-*- coding:utf-8 -*-

import tkinter as tk                # python 3
import tkinter.ttk
import threading
import platform

from setting_page import *
if platform.system() == "Linux" :
    from range_finder import *
    import RPi.GPIO as GPIO
    from hx711 import HX711

import time

from spray_mode import *
from config_manager import *
from config_value import ConfigValue
from liquid_balance_manager import LiquidBalanceManager

import sys
import random #테스트용
import threading
import pygame

class StartPage(SettingPage):

    def __init__(self, parent, controller, background_img):
        super().__init__(parent, controller, background_img)
        self.controller = controller
        self.init_UI()
        self.init_WPI()
        self.spray_start_time = None
        self.out_valve_start_time = None
        self.auto_thread = None

        self.referenceUnit = 1
        self.hx = None
        pygame.init()
        pygame.mixer.init()
        self.liquid_10per = False
        self.liquid_5per = False

    def init_UI(self):

        self.imgBtnDetect01 = tk.PhotoImage(file='images/btnDetect01.png')
        self.imgBtnDetect02 = tk.PhotoImage(file='images/btnDetect02.png')
        self.imgBtnAuto01 = tk.PhotoImage(file='images/btnAuto01.png')
        self.imgBtnAuto02 = tk.PhotoImage(file='images/btnAuto02.png')
        self.imgBtnManual01 = tk.PhotoImage(file='images/btnManual01.png')
        self.imgBtnManual02 = tk.PhotoImage(file='images/btnManual02.png')
        self.settingBtnImg = tk.PhotoImage(file='images/btn_01.png')

        
        self.btnMode1 = tk.Button(self.frame, image=self.imgBtnDetect01, relief=tk.SOLID, command=lambda: self.changeSprayMode(SprayMode.DETECT,self.btnMode1), bd=0, highlightthickness=0, bg=self.COLOR_BUTTON_BACKGROUND)
        self.btnMode2 = tk.Button(self.frame, image=self.imgBtnAuto01, relief=tk.SOLID, command=lambda: self.changeSprayMode(SprayMode.AUTO,self.btnMode2), bd=0, highlightthickness=0, bg=self.COLOR_BUTTON_BACKGROUND)
        self.btnMode3 = tk.Button(self.frame, image=self.imgBtnManual01, relief=tk.SOLID, command=lambda: self.changeSprayMode(SprayMode.MANUAL,self.btnMode3), bd=0, highlightthickness=0, bg=self.COLOR_BUTTON_BACKGROUND)


        self.btnMode4 = tk.Button(self.frame, relief=tk.SOLID, bd=0, highlightthickness=0, image=self.settingBtnImg, command=lambda: self.controller.show_frame("DetectPage"), bg=self.COLOR_BUTTON_BACKGROUND)
        self.btnMode5 = tk.Button(self.frame, relief=tk.SOLID, bd=0, highlightthickness=0, image=self.settingBtnImg, command=lambda: self.controller.show_frame("AutoPage"), bg=self.COLOR_BUTTON_BACKGROUND)

        self.btnMode1.place(relx=0.1, rely=0.2-0.03)
        self.btnMode2.place(relx=0.4, rely=0.2-0.03)
        self.btnMode3.place(relx=0.7, rely=0.2-0.03)
        self.btnMode4.place(relx=0.18, rely=0.6-0.03)
        self.btnMode5.place(relx=0.49, rely=0.6-0.03)

        self.progressbar_style = tkinter.ttk.Style()
        self.progressbar_style.theme_use('default')
        self.progressbar_style.configure("TProgressbar", foreground='green', background='green', thickness=30)

        font=tkinter.font.Font(family="맑은 고딕", size=11)
        self.progressbar = tkinter.ttk.Progressbar(self.frame, style="TProgressbar", maximum=100, mode="determinate", value=50, length=800)
        self.progressbar.place(relx=0.11, rely=0.7)
        self.label_liquid_balance = tkinter.Label(self.frame, text="약재잔량 : 100%", fg="white", relief="flat", bg="#0C4323", font=font)
        self.label_liquid_balance.place(relx=0.78, rely=0.65)

        self.start_check_liquid_balance()

        self.modeBtnCheck()
        if platform.system() == "Linux" :
            self.rangeFinder = RangeFinder()


    def start_check_liquid_balance(self):
        if platform.system() == "Linux" :
            self.hx = HX711(17, 27)
            self.hx.set_reading_format("MSB", "MSB")
            self.hx.set_reading_format("MSB", "MSB")
            self.hx.reset()
            self.hx.tare()


        t = threading.Thread(target=self.bg_worker)
        t.start()

    def update_liquid_balance(self, liquid_balance):
        self.label_liquid_balance.configure(text = "약재잔량 : " + str(liquid_balance) + "%")
        self.progressbar.configure(value=liquid_balance)

        self.liquid_5per = False
        if liquid_balance >= 0 and liquid_balance <= 10:
            color_value = 'red'
            if self.liquid_10per == False:
                self.liquid_10per = True
                self.play_notice_10per_sound()
            if liquid_balance <= 5:
                self.liquid_5per = True

        elif liquid_balance > 10 and liquid_balance <= 30:
            color_value = 'yellow'
        elif liquid_balance > 30 and liquid_balance <= 100:
            color_value = 'green'
            self.liquid_10per = False
        else:
            color_value = 'green'
            self.liquid_10per = False
            
        self.progressbar_style.configure("TProgressbar", foreground=color_value, background=color_value, thickness=30)


    def modeBtnCheck(self):
        self.btnMode1.configure(image = self.imgBtnDetect01)
        self.btnMode2.configure(image = self.imgBtnAuto01)
        self.btnMode3.configure(image = self.imgBtnManual01)

        spray_mode = ConfigManager().get_value("spray_mode")
       
        if spray_mode == SprayMode.DETECT :
            self.btnMode1.configure(image = self.imgBtnDetect02)
        elif spray_mode == SprayMode.AUTO :
            self.btnMode2.configure(image = self.imgBtnAuto02)
        elif spray_mode == SprayMode.MANUAL :
            self.btnMode3.configure(image = self.imgBtnManual02)

    def init_WPI(self):
        if super().is_linux_system():
            GPIO.setmode(GPIO.BCM)
            GPIO.output(ConfigValue.SPRAY_WPI_NUM, False)
            GPIO.output(ConfigValue.VALVE_WPI_NUM, False)


    def strToSpraymMode(self, str) :
        if str == "SprayMode.AUTO":
            return SprayMode.AUTO
        elif str == "SprayMode.DETECT":
            return SprayMode.DETECT
        elif str == "SprayMode.MANUAL":
            return SprayMode.MANUAL

    def changeSprayMode(self, sprayMode, btnObj):
        ConfigManager().set_value("spray_mode", sprayMode)

        if sprayMode == SprayMode.DETECT :
            self.refresher()
        elif sprayMode == SprayMode.AUTO :
            if self.auto_thread != None:
                if self.auto_thread.is_alive():
                    self.auto_thread.cancel()

            self.startAuto()
        elif sprayMode == SprayMode.MANUAL:
            self.controller.show_frame("ManualPage")
        
        self.modeBtnCheck()

    def refresher(self):
        if ConfigManager().get_value("spray_mode") == SprayMode.DETECT:
            if platform.system() == "Linux" :
                distance = self.rangeFinder.read(liquid_5per)
            self.after(10, self.refresher) # every second...

    def startAuto(self):
        if ConfigManager().get_value("spray_mode") == SprayMode.AUTO:
            self.spray_start_time = time.time()
            self.sprayByTime()
        else:
            return True
        
        print("automode cycle")
        self.auto_thread = threading.Timer(int(ConfigManager().get_value("auto_cycle_min")) * 60, self.startAuto)
        self.auto_thread.start()

    def sprayByTime(self):
        if ConfigManager().get_value("spray_mode") == SprayMode.AUTO and time.time() - self.spray_start_time < int(ConfigManager().get_value("auto_spray_duration_sec")):
            if platform.system() == "Linux":
                self.spray_on()
        else:
            if platform.system() == "Linux":
                self.spray_off()
            return True
        threading.Timer(0.5, self.sprayByTime).start()

    def spray_on(self):
        if self.liquid_5per == False :
            GPIO.output(ConfigValue.SPRAY_WPI_NUM, True)
            GPIO.output(ConfigValue.VALVE_WPI_NUM, False)
    
    def spray_off(self):
        GPIO.output(ConfigValue.SPRAY_WPI_NUM, False)
        self.out_valve_start_time = time.time()
        self.on_out_valve()


    def on_out_valve(self):
        if time.time() - self.out_valve_start_time < ConfigValue.VALVE_ON_TIME:
            if platform.system() == "Linux":
                GPIO.output(ConfigValue.VALVE_WPI_NUM, True)
        else:
            if platform.system() == "Linux":
                GPIO.output(ConfigValue.VALVE_WPI_NUM, False)
            return True
        threading.Timer(0.1, self.on_out_valve).start()

    def bg_worker(self):
        hx = HX711(17, 27)
        hx.set_reading_format("MSB", "MSB")
        hx.set_reading_format("MSB", "MSB")
        hx.reset()
        hx.tare()

        unit_value = 92
        full_weight = 20000 #그램
        empty_weight = 500 #그램

        while True:
            try:
                val = hx.get_weight(5)
                hx.power_down()
                hx.power_up()
                
                gram = val / unit_value
                
                print("test=======val : " + str(val))
                print("test=======gram : " + str(gram))

                if val < 0 :
                    weight_ratio = 0
                else :
                    if gram < empty_weight :
                        weight_ratio = 0
                    elif gram > full_weight :
                        weight_ratio = 100
                    else :
                        print("test===========full_weight / gram : " + str(full_weight / gram))
                        weight_ratio = round((gram / full_weight) * 100)
                        
                print("test==============weight_ratio : " + str(weight_ratio))

                self.update_liquid_balance(weight_ratio)

                time.sleep(1)
            except (KeyboardInterrupt, SystemExit):
                self.cleanAndExit()

        """
        while True:
            val = random.randint(1,10)
            self.update_liquid_balance(val * 10)
            time.sleep(1)
        """

    def cleanAndExit(self):
        GPIO.cleanup()
        sys.exit()

    def play_notice_10per_sound(self):
        notice_10per_sound = pygame.mixer.Sound('./sound/notice_10per.wav')
        notice_10per_sound.set_volume(1)
        if self.liquid_10per :
            notice_10per_sound.play()
        else:
            return
        threading.Timer(30, self.play_notice_10per_sound).start()