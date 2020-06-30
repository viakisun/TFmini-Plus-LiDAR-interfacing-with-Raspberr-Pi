#-*- coding:utf-8 -*-

import platform
import tkinter as tk                # python 3
if platform.system() == "Linux" :
    import odroid_wiringpi as wpi
    from RangeFinder import *

from SprayMode import *


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Relay
        if platform.system() == "Linux" :
            wpi.wiringPiSetup()
            wpi.pinMode(4, 1)
        
        frameButton = tk.Frame(self, relief="solid", bg="red", height=60)
        frameButton.pack(side="left", fill="both", expand=True)
        background_label = tk.Label(frameButton, image=controller.img01)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.btnMode1 = tk.Button(frameButton, image=controller.imgBtnDistance01, relief="ridge", command=lambda: self.changeSprayMode(SprayMode.DISTANCE,self.btnMode1), bd=0, bg="#0C4323")
        self.btnMode2 = tk.Button(frameButton, image=controller.imgBtnAuto01, relief="solid", command=lambda: self.changeSprayMode(SprayMode.AUTO,self.btnMode2), bd=0, bg="#0C4323")
        self.btnMode3 = tk.Button(frameButton, image=controller.imgBtnManual01, relief="solid", command=lambda: self.changeSprayMode(SprayMode.MANUAL,self.btnMode3), bd=0, bg="#0C4323")
        self.btnMode4 = tk.Button(frameButton, relief="solid", bd=0, image=controller.settingBtnImg, command=lambda: controller.show_frame("DistanceModePage"), bg="#0C4323")
        self.btnMode5 = tk.Button(frameButton, relief="solid", bd=0, image=controller.settingBtnImg, command=lambda: controller.show_frame("DistanceModePage"), bg="#0C4323")

        self.btnMode1.place(relx=0.1, rely=0.25)
        self.btnMode2.place(relx=0.4, rely=0.25)
        self.btnMode3.place(relx=0.7, rely=0.25)
        self.btnMode4.place(relx=0.18, rely=0.65)
        self.btnMode5.place(relx=0.49, rely=0.65)
       
        self.modeBtnCheck()
        if platform.system() == "Linux" :
            self.rangeFinder = RangeFinder(controller)

    def modeBtnCheck(self):
        self.btnMode1.configure(image = self.controller.imgBtnDistance01)
        self.btnMode2.configure(image = self.controller.imgBtnAuto01)
        self.btnMode3.configure(image = self.controller.imgBtnManual01)

        if self.controller.sprayMode == SprayMode.DISTANCE :
            self.btnMode1.configure(image = self.controller.imgBtnDistance02)
        elif self.controller.sprayMode == SprayMode.AUTO :
            self.btnMode2.configure(image = self.controller.imgBtnAuto02)
        elif self.controller.sprayMode == SprayMode.MANUAL :
            self.btnMode3.configure(image = self.controller.imgBtnManual02)

    def sprayStart(self):
        if self.manualSprayOn :
            if platform.system() == "Linux" :
                wpi.digitalWrite(4, 0)
            self.manualSprayOn = False
        else :
            if platform.system() == "Linux" :
                wpi.digitalWrite(4, 1)
            self.manualSprayOn = True


    def changeSprayMode(self,sprayMode,btnObj):
        if sprayMode == SprayMode.DISTANCE :
            if self.controller.sprayMode == SprayMode.DISTANCE :
                self.refresher()
        elif sprayMode == SprayMode.AUTO :
            return False
        elif sprayMode == SprayMode.MANUAL:
            if self.controller.sprayMode == SprayMode.MANUAL :
                self.controller.show_frame("ManualPage")
        else:
            return False

        self.controller.setSprayMode(sprayMode)
        self.modeBtnCheck()

    def refresher(self):
        distance = self.rangeFinder.read()
        print(str(distance))
        if self.controller.sprayMode == SprayMode.DISTANCE :
            self.after(10, self.refresher) # every second...