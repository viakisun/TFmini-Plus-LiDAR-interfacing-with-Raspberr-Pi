import tkinter as tk                # python 3
import odroid_wiringpi as wpi
from SprayMode import *

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.strSprayMode = tk.StringVar()
        self.strSprayMode.set(controller.getSprayModeStr())
        self.manualSprayOn = False;

        # Relay
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
        self.btnMode3 = tk.Button(frameButton, text="수동분사", font=controller.modebutton_font, relief="solid", command=lambda: self.sprayStart())
        self.btnMode4 = tk.Button(frameButton, relief="solid", bd=0, image=controller.settingBtnImg, command=lambda: controller.show_frame("DistanceModePage"))
        self.btnMode5 = tk.Button(frameButton, relief="solid", bd=0, image=controller.settingBtnImg)

        self.btnMode1.place(relwidth=0.2, relheight=0.6, relx=0.1, rely=0.1)
        self.btnMode2.place(relwidth=0.2, relheight=0.6, relx=0.4, rely=0.1)
        self.btnMode3.place(relwidth=0.2, relheight=0.6, relx=0.7, rely=0.1)
        self.btnMode4.place(relx=0.17, rely=0.75)
        self.btnMode5.place(relx=0.47, rely=0.75)

    def sprayStart(self):
        if self.manualSprayOn :
            wpi.digitalWrite(4, 0)
            self.manualSprayOn = False
        else :
            wpi.digitalWrite(4, 1)
            self.manualSprayOn = True

    def changeSprayMode(self,sprayMode,btnObj):
        self.btnMode1.configure(bg = "#f5f5f5")
        self.btnMode2.configure(bg = "#f5f5f5")
        self.btnMode3.configure(bg = "#f5f5f5")
        btnObj.configure(bg = "green")

        self.controller.setSprayMode(sprayMode)
        self.strSprayMode.set(self.controller.getSprayModeStr())