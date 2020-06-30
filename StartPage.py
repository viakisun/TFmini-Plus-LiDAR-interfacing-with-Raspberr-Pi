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

        self.strSprayMode = tk.StringVar()
        self.strSprayMode.set(controller.getSprayModeStr())
        self.manualSprayOn = False;

        # Relay
        if platform.system() == "Linux" :
            wpi.wiringPiSetup()
            wpi.pinMode(4, 1)
        
        #상단메뉴
        frameTop = tk.Frame(self, relief="solid", bg="#222222", height=60)
        frameTop.pack(side="top", fill="x")
        label1 = tk.Label(frameTop, text="  현재 분사모드 : ", fg="white", bg="#222222", height=3)
        label1.pack(side="left")
        lblMode = tk.Label(frameTop, fg="white", bg="#222222", height=3, textvariable=self.strSprayMode)
        lblMode.pack(side="left")
        
        #모드버튼
        frameButton = tk.Frame(self, relief="solid", bg="white", height=60)
        frameButton.pack(side="left", fill="both", expand=True)

        self.btnMode1 = tk.Button(frameButton, text="거리인식 모드", font=controller.modebutton_font, relief="solid", command=lambda: self.changeSprayMode(SprayMode.DISTANCE,self.btnMode1))
        self.btnMode2 = tk.Button(frameButton, text="자동모드", font=controller.modebutton_font, relief="solid", command=lambda: self.changeSprayMode(SprayMode.AUTO,self.btnMode2))
        self.btnMode3 = tk.Button(frameButton, text="수동분사", font=controller.modebutton_font, relief="solid", command=lambda: self.changeSprayMode(SprayMode.MANUAL,self.btnMode3))
        self.btnMode4 = tk.Button(frameButton, relief="solid", bd=0, image=controller.settingBtnImg, command=lambda: controller.show_frame("DistanceModePage"))
        self.btnMode5 = tk.Button(frameButton, relief="solid", bd=0, image=controller.settingBtnImg)

        self.btnMode1.place(relwidth=0.2, relheight=0.6, relx=0.1, rely=0.1)
        self.btnMode2.place(relwidth=0.2, relheight=0.6, relx=0.4, rely=0.1)
        self.btnMode3.place(relwidth=0.2, relheight=0.6, relx=0.7, rely=0.1)
        self.btnMode4.place(relx=0.17, rely=0.75)
        self.btnMode5.place(relx=0.47, rely=0.75)

        if platform.system() == "Linux" :
            self.rangeFinder = RangeFinder()

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
        self.btnMode1.configure(bg = "#f5f5f5")
        self.btnMode2.configure(bg = "#f5f5f5")
        self.btnMode3.configure(bg = "#f5f5f5")
        btnObj.configure(bg = "green")

        if sprayMode == SprayMode.DISTANCE :
            if self.controller.sprayMode == SprayMode.DISTANCE :
                self.refresher()
        elif sprayMode == SprayMode.AUTO :
            return False
        elif sprayMode == SprayMode.MANUAL:
            if self.controller.sprayMode == SprayMode.MANUAL :
                self.sprayStart()
        else:
            return False

        self.controller.setSprayMode(sprayMode)
        self.strSprayMode.set(self.controller.getSprayModeStr())

    def refresher(self):
        distance = self.rangeFinder.read()
        print(str(distance))
        self.after(10, self.refresher) # every second...