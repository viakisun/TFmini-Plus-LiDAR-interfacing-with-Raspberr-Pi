#-*- coding:utf-8 -*-

import platform
import tkinter as tk                # python 3
if platform.system() == "Linux" :
    import odroid_wiringpi as wpi

from SprayMode import *

class ManualPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Relay
        if platform.system() == "Linux" :
            wpi.wiringPiSetup()
            wpi.pinMode(4, 1)
        
        frame = tk.Frame(self, relief="solid", bg="red", height=60)
        frame.pack(side="left", fill="both", expand=True)
        background_label = tk.Label(frame, image=controller.img04)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        btnHome = tk.Button(frame, relief="solid", bd=0, image=controller.imgBtnBack, bg="#0C4323", command=lambda: controller.show_frame("StartPage"))
        btnHome.place(relx=0.93, rely=0.03)

        self.btnSprayOn = tk.Button(frame, image=controller.imgBtnSprayOn, relief="ridge", bd=0, bg="#0C4323", command=lambda: self.sprayOn())
        self.btnSprayOff = tk.Button(frame, image=controller.imgBtnSprayOff, relief="ridge", bd=0, bg="#0C4323", command=lambda: self.sprayOff())

        self.btnSprayOn.place(relx=0.22, rely=0.35)
        self.btnSprayOff.place(relx=0.55, rely=0.35)

    def sprayOn(self):
        if platform.system() == "Linux" :
            wpi.digitalWrite(4, 1)

    def sprayOff(self):
        if platform.system() == "Linux" :
            wpi.digitalWrite(4, 0)