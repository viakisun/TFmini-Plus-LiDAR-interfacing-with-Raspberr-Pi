#-*- coding:utf-8 -*-
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from config_value import ConfigValue
from setting_page import *
from config_manager import ConfigManager

class AutoPage(SettingPage):

    def __init__(self, parent, controller, background_img):
        super().__init__(parent, controller, background_img)
        self.controller = controller
        self.init_UI()


    def init_UI(self):

        self.sprayTimeVar = tk.StringVar()
        self.sprayTimeVar.set(str(ConfigManager().get_value("auto_spray_duration_sec")))

        self.cycleTimeVar = tk.StringVar()
        self.cycleTimeVar.set(str(ConfigManager().get_value("auto_cycle_min")))
        self.btnHome.place(relx=0.93, rely=0.03)
        
        #분사주기 조절
        lblCycleTime = tk.Label(self.frame, fg="white", bg=self.COLOR_BUTTON_BACKGROUND, font=tkfont.Font(size=50, weight="bold"), textvariable=self.cycleTimeVar, anchor="e", padx=10)
        lblCycleTime.place(relx=0.45, rely=0.36, relwidth=0.18, relheight=0.18)

        btnCycleTimeUp = tk.Button(self.frame, relief="solid", bd=0, highlightthickness=0, command=lambda: self.upCycleTime(), image=self.imgBtnUp, bg=self.COLOR_BUTTON_BACKGROUND)
        btnCycleTimeUp.place(relx=0.66, rely=0.38)
        
        btnCycleTimeDown = tk.Button(self.frame, relief="solid", bd=0, highlightthickness=0, command=lambda: self.downCycleTime(), image=self.imgBtnDown, bg=self.COLOR_BUTTON_BACKGROUND)
        btnCycleTimeDown.place(relx=0.76, rely=0.38)
       
        #분사시간 조절
        lblTime = tk.Label(self.frame, fg="white", bg=self.COLOR_BUTTON_BACKGROUND, font=tkfont.Font(size=50, weight="bold"), textvariable=self.sprayTimeVar, anchor="e", padx=10)
        lblTime.place(relx=0.45, rely=0.36 + 0.22, relwidth=0.18, relheight=0.18)

        btnTimeUp = tk.Button(self.frame, image=self.imgBtnUp, relief="solid", bd=0, highlightthickness=0, bg=self.COLOR_BUTTON_BACKGROUND, command=lambda: self.upTime())
        btnTimeUp.place(relx=0.66, rely=0.38 + 0.22)
        
        btnTimeDown = tk.Button(self.frame, image=self.imgBtnDown, relief="solid", bd=0, highlightthickness=0, bg=self.COLOR_BUTTON_BACKGROUND, command=lambda: self.downTime())
        btnTimeDown.place(relx=0.76, rely=0.38 + 0.22)


    def upTime(self):
        ATTRIBUTE_ = "auto_spray_duration_sec"
        INCREMENT_ = 1
        MAX_ = 100

        value_ = self.get_value(ATTRIBUTE_)
        str_value_ = str(value_ + INCREMENT_)

        if value_ < MAX_ :
            self.set_value(ATTRIBUTE_, str_value_)
            self.sprayTimeVar.set(str_value_)

    def downTime(self):
        ATTRIBUTE_ = "auto_spray_duration_sec"
        INCREMENT_ = 1
        MIN_ = 3

        value_ = self.get_value(ATTRIBUTE_)
        str_value_ = str(value_ - INCREMENT_)

        if value_ > MIN_ :
            self.set_value(ATTRIBUTE_, str_value_)
            self.sprayTimeVar.set(str_value_)

    def upCycleTime(self):
        ATTRIBUTE_ = "auto_cycle_min"
        INCREMENT_ = 1
        MAX_ = 100

        value_ = self.get_value(ATTRIBUTE_)
        str_value_ = str(value_ + INCREMENT_)

        if value_ < MAX_ :
            self.set_value(ATTRIBUTE_, str_value_)
            self.cycleTimeVar.set(str_value_)

    def downCycleTime(self):
        ATTRIBUTE_ = "auto_cycle_min"
        INCREMENT_ = 1
        MIN_ = 3

        value_ = self.get_value(ATTRIBUTE_)
        str_value_ = str(value_ - INCREMENT_)

        if value_ > MIN_ :
            self.set_value(ATTRIBUTE_, str_value_)
            self.cycleTimeVar.set(str_value_)

    def get_value(self, attribute_):
        return int(ConfigManager().get_value(attribute_))

    def set_value(self, attribute_, value_):
        ConfigManager().set_value(attribute_, value_)       