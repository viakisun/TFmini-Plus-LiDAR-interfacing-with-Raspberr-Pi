#-*- coding:utf-8 -*-
import tkinter as tk                # python 3
from setting_page import *

if platform.system() == "Linux" :
    import odroid_wiringpi as wpi

class ManualPage(SettingPage):

    def __init__(self, parent, controller, background_img):
        super().__init__(parent, controller, background_img)
        self.init_UI()
        self.init_WPI()
        self.spray_on_check = False
        self.change_spray_btn()

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

    def init_WPI(self):
        if super().is_linux_system():
            wpi.wiringPiSetup()
            wpi.pinMode(4, 1)
            wpi.digitalWrite(4, 0)

    def spray_on(self):
        if super().is_linux_system():
            wpi.digitalWrite(4, 1)
        self.spray_on_check = True
        self.change_spray_btn()

    def spray_off(self):
        if super().is_linux_system():
            wpi.digitalWrite(4, 0)
        self.spray_on_check = False
        self.change_spray_btn()            

    def change_spray_btn(self):
        if self.spray_on_check:
            self.btn_spray_on.configure(image = self.img_btn_spray_on_sel)
            self.btn_spray_off.configure(image = self.img_btn_spray_off)
        else:
            self.btn_spray_on.configure(image = self.img_btn_spray_on)
            self.btn_spray_off.configure(image = self.img_btn_spray_off_sel)         