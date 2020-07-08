#-*- coding:utf-8 -*-
import tkinter as tk                # python 3
from SettingPage import *

class ManualPage(SettingPage):

    def __init__(self, parent, controller, background_img):
        super().__init__(parent, controller, background_img)
        self.init_UI()
        self.init_WPI()

    def init_UI(self):
        RELIEF_STYLE = "ridge"

        self.img_btn_spray_on = tk.PhotoImage(file='images/btn_spray_on.png')
        self.img_btn_spray_off = tk.PhotoImage(file='images/btn_spray_off.png')

        btn_spray_on = tk.Button(self.frame, image=self.img_btn_spray_on, relief=RELIEF_STYLE, bd=0, bg=self.COLOR_BUTTON_BACKGROUND, command=lambda: self.spray_on())
        btn_spray_off = tk.Button(self.frame, image=self.img_btn_spray_off, relief=RELIEF_STYLE, bd=0, bg=self.COLOR_BUTTON_BACKGROUND, command=lambda: self.spray_off())
        btn_spray_on.place(relx=0.22, rely=0.35)
        btn_spray_off.place(relx=0.55, rely=0.35)
        self.btnHome.place(relx=0.93, rely=0.03)

    def init_WPI(self):
        if super().is_linux_system():
            wpi.wiringPiSetup()
            wpi.pinMode(4, 1)

    def spray_on(self):
        if super().is_linux_system():
            wpi.digitalWrite(4, 1)

    def spray_off(self):
        if super().is_linux_system():
            wpi.digitalWrite(4, 0)