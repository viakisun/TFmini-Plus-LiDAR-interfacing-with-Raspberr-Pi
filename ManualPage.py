#-*- coding:utf-8 -*-

import tkinter as tk                # python 3

from SprayMode import *

class ManualPage(SettingPage):

    def __init__(self, parent, controller, background_img):
        super(self, ).__init__(self, parent, background_img)
        self.init_UI()
        self.init_WPI()

    def init_UI(self):
        COLOR_BUTTON_BACKGROUND = "#0C4323"
        RELIEF_STYLE = "ridge"

        img_btn_spray_on = tk.PhotoImage(file='images/btn_spray_on.png')
        img_btn_spray_off = tk.PhotoImage(file='images/btn_spray_off.png')

        btn_spray_on = tk.Button(frame, image=img_btn_spray_on, relief=RELIEF_STYLE, bd=0, bg=COLOR_BUTTON_BACKGROUND, command=lambda: self.spray_on())
        btn_spray_off = tk.Button(frame, image=img_btn_spray_off, relief=RELIEF_STYLE, bd=0, bg=COLOR_BUTTON_BACKGROUND, command=lambda: self.spray_off())
        btn_spray_on.place(relx=0.22, rely=0.35)
        btn_spray_off.place(relx=0.55, rely=0.35)

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