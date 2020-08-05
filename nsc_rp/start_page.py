#-*- coding:utf-8 -*-

import tkinter as tk                # python 3
import threading
import platform
from setting_page import *
if platform.system() == "Linux" :
    from range_finder import *
    import RPi.GPIO as GPIO

import time
from spray_mode import *
from config_manager import *
from config_value import ConfigValue

class StartPage(SettingPage):

    def __init__(self, parent, controller, background_img):
        super().__init__(parent, controller, background_img)
        self.controller = controller
        self.init_UI()
        self.init_WPI()
        self.spray_start_time = None
        self.out_valve_start_time = None
        self.auto_thread = None

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

        self.btnMode1.place(relx=0.1, rely=0.25)
        self.btnMode2.place(relx=0.4, rely=0.25)
        self.btnMode3.place(relx=0.7, rely=0.25)
        self.btnMode4.place(relx=0.18, rely=0.65)
        self.btnMode5.place(relx=0.49, rely=0.65)

        self.modeBtnCheck()
        if platform.system() == "Linux" :
            self.rangeFinder = RangeFinder()

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
                distance = self.rangeFinder.read()
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
        GPIO.output(ConfigValue.SPRAY_WPI_NUM, True)
        
    
    def spray_off(self):
        GPIO.output(ConfigValue.SPRAY_WPI_NUM, False)
        self.out_valve_start_time = time.time()