#-*- coding:utf-8 -*-
import tkinter as tk                # python 3
from setting_page import *

if platform.system() == "Linux" :
    import RPi.GPIO as GPIO

import time
import threading
from config_value import ConfigValue    

class ManualPage(SettingPage):

    def __init__(self, parent, controller, background_img):
        super().__init__(parent, controller, background_img)
        self.init_UI()
        self.init_spray()
        self.change_spray_btn()
        self.out_valve_start_time = None

    def init_UI(self):
        self.img_btn_spray_on = tk.PhotoImage(file='images/btn_spray_on.png')
        self.img_btn_spray_off = tk.PhotoImage(file='images/btn_spray_off.png')
        self.img_btn_spray_on_sel = tk.PhotoImage(file='images/btn_spray_on_sel.png')
        self.img_btn_spray_off_sel = tk.PhotoImage(file='images/btn_spray_off_sel.png')

        self.btn_spray_on = tk.Button(self.frame, image=self.img_btn_spray_on, relief=tk.RIDGE, bd=0, highlightthickness=0, bg=self.COLOR_BUTTON_BACKGROUND, command=lambda: self.spray_on())
        self.btn_spray_off = tk.Button(self.frame, image=self.img_btn_spray_off, relief=tk.RIDGE, bd=0, highlightthickness=0, bg=self.COLOR_BUTTON_BACKGROUND, command=lambda: self.spray_off())
        self.btn_spray_on.place(relx=0.22, rely=0.35)
        self.btn_spray_off.place(relx=0.55, rely=0.35)
        self.btnHome.place(relx=0.93, rely=0.03)

    def init_spray(self):
        self.spray_on_check = False
        if super().is_linux_system():
            GPIO.setmode(GPIO.BCM)
            GPIO.output(ConfigValue.SPRAY_WPI_NUM, False)
            GPIO.output(ConfigValue.VALVE_WPI_NUM, False)

    def spray_on(self):
        if super().is_linux_system():
            GPIO.output(ConfigValue.SPRAY_WPI_NUM, True)
            GPIO.output(ConfigValue.VALVE_WPI_NUM, False)

        self.spray_on_check = True
        self.change_spray_btn()

    def spray_off(self):
        if super().is_linux_system():
            GPIO.output(ConfigValue.SPRAY_WPI_NUM, False)
            self.out_valve_start_time = time.time()
            self.on_out_valve()
        self.spray_on_check = False
        self.change_spray_btn()            

    def change_spray_btn(self):
        if self.spray_on_check:
            self.btn_spray_on.configure(image = self.img_btn_spray_on_sel)
            self.btn_spray_off.configure(image = self.img_btn_spray_off)
        else:
            self.btn_spray_on.configure(image = self.img_btn_spray_on)
            self.btn_spray_off.configure(image = self.img_btn_spray_off_sel)

    def on_out_valve(self):
        if time.time() - self.out_valve_start_time < ConfigValue.VALVE_ON_TIME:
            if platform.system() == "Linux":
                GPIO.output(ConfigValue.VALVE_WPI_NUM, True)
        else:
            if platform.system() == "Linux":
                GPIO.output(ConfigValue.VALVE_WPI_NUM, False)
            return True
        threading.Timer(0.1, self.on_out_valve).start()