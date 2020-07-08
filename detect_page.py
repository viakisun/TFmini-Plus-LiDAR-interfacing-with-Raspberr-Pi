#-*- coding:utf-8 -*-
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from setting_page import *
from config_manager import *
from config_value import ConfigValue

class DetectPage(SettingPage):

    def __init__(self, parent, controller, background_img):
        super().__init__(parent, controller, background_img)
        self.controller = controller
        self.init_UI()

    def init_UI(self):

        # tk.Frame.__init__(self, parent)
        self.sprayTimeVar = tk.StringVar()
        self.sprayTimeVar.set(str(ConfigManager().get_value("detect_spray_duration_sec")))

        self.detectDistanceVar = tk.StringVar()
        self.detectDistanceVar.set(str(ConfigManager().get_value("detect_distance_meter")))
        self.btnHome.place(relx=0.93, rely=0.03)

        #인식거리 조절
        lblDistance = tk.Label(self.frame, fg="white", bg="#467E39", font=tkfont.Font(size=50, weight="bold"), textvariable=self.detectDistanceVar, anchor="e", padx=10)
        lblDistance.place(relx=0.45, rely=0.36, relwidth=0.18, relheight=0.18)

        btnDistanceUp = tk.Button(self.frame, relief="solid", bd=0, command=lambda: self.set_distance_up(), image=self.imgBtnUp, bg=self.COLOR_BUTTON_BACKGROUND)
        btnDistanceUp.place(relx=0.66, rely=0.38)
        
        btnDistanceDown = tk.Button(self.frame, relief="solid", bd=0, command=lambda: self.set_distance_down(), image=self.imgBtnDown, bg=self.COLOR_BUTTON_BACKGROUND)
        btnDistanceDown.place(relx=0.76, rely=0.38)
       
        #오른쪽 분사시간 조절
        lblTime = tk.Label(self.frame, fg="white", bg="#467E39", font=tkfont.Font(size=50, weight="bold"), textvariable=self.sprayTimeVar, anchor="e", padx=10)
        lblTime.place(relx=0.45, rely=0.36 + 0.22, relwidth=0.18, relheight=0.18)

        btnTimeUp = tk.Button(self.frame, image=self.imgBtnUp, relief="solid", bd=0, bg=self.COLOR_BUTTON_BACKGROUND, command=lambda: self.upTime())
        btnTimeUp.place(relx=0.66, rely=0.38 + 0.22)
        
        btnTimeDown = tk.Button(self.frame, image=self.imgBtnDown, relief="solid", bd=0, bg=self.COLOR_BUTTON_BACKGROUND, command=lambda: self.downTime())
        btnTimeDown.place(relx=0.76, rely=0.38 + 0.22)

    def upTime(self):
        if float(ConfigManager().get_value("detect_spray_duration_sec")) < ConfigValue.MAX_SPRAY_TIME :
            ConfigManager().set_value("detect_spray_duration_sec", float(ConfigManager().get_value("detect_spray_duration_sec")) + 0.5)
        self.sprayTimeVar.set(str(ConfigManager().get_value("detect_spray_duration_sec")))

    def downTime(self):
        if float(ConfigManager().get_value("detect_spray_duration_sec")) > ConfigValue.MIN_SPRAY_TIME :
            ConfigManager().set_value("detect_spray_duration_sec", float(ConfigManager().get_value("detect_spray_duration_sec")) - 0.5)
        self.sprayTimeVar.set(str(ConfigManager().get_value("detect_spray_duration_sec")))

    def set_distance_up(self):
        ATTRIBUTE_ = "detect_distance_meter"
        INCREMENT_ = 0.1
        ROUND_DIGIT_ = 1
        MAX_DETECT_DISTANCE = 3.0

        value_ = self.get_value(ATTRIBUTE_)
        str_value_ = str(round(value_ + INCREMENT_, ROUND_DIGIT_))

        if value_ < MAX_DETECT_DISTANCE :
            self.set_value(ATTRIBUTE_, str_value_)
            self.detectDistanceVar.set(str_value_)

    def set_distance_down(self):
        ATTRIBUTE_ = "detect_distance_meter"
        INCREMENT_ = 0.1
        ROUND_DIGIT_ = 1
        MIN_DETECT_DISTANCE = 0.5

        value_ = self.get_value(ATTRIBUTE_)
        str_value_ = str(round(value_ - INCREMENT_, ROUND_DIGIT_))

        if value_ > MIN_DETECT_DISTANCE :
            self.set_value(ATTRIBUTE_, str_value_)
            self.detectDistanceVar.set(str_value_)

    def get_value(self, attribute_):
        return round(float(ConfigManager().get_value(attribute_)), 1)

    def set_value(self, attribute_, value_):
        ConfigManager().set_value(attribute_, value_)       