#-*- coding:utf-8 -*-

import tkinter as tk                # python 3
import threading
import platform
from setting_page import *
if platform.system() == "Linux" :
    from range_finder import *
    import odroid_wiringpi as wpi

import time

from spray_mode import *
from config_manager import *


class StartPage(SettingPage):

    def __init__(self, parent, controller, background_img):
        super().__init__(parent, controller, background_img)
        self.controller = controller
        self.init_UI()
        self.init_WPI()
        self.spray_start_time = None

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
            wpi.wiringPiSetup()
            wpi.pinMode(4, 1)
            wpi.digitalWrite(4, 0)


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
        #threading.Timer(int(ConfigManager().get_value("auto_cycle_min")) * 60, self.startAuto).start()
        print("automode cycle")
        threading.Timer(10, self.startAuto).start()

    # def autoByTime(self):
        

    def sprayByTime(self):
        if ConfigManager().get_value("spray_mode") == SprayMode.AUTO and time.time() - self.spray_start_time < int(ConfigManager().get_value("auto_spray_duration_sec")):
            if platform.system() == "Linux":
                wpi.digitalWrite(4, 1)
        else:
            if platform.system() == "Linux":
                wpi.digitalWrite(4, 0)
            return True            

        threading.Timer(0.5, self.sprayByTime).start()

        #threading.Timer(int(ConfigManager().get_value("auto_cycle_min")) * 60, self.sprayByTime).start()
