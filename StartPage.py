import tkinter as tk                # python 3
import odroid_wiringpi as wpi

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.strSprayMode = tk.StringVar()
        self.strSprayMode.set("수동분사")
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

        btnMode1 = tk.Button(frameButton, text="거리인식 모드", font=controller.modebutton_font, relief="solid", bd=0)
        btnMode2 = tk.Button(frameButton, text="자동모드", font=controller.modebutton_font, relief="solid", bd=0)
        btnMode3 = tk.Button(frameButton, text="수동분사", font=controller.modebutton_font, relief="solid", bd=2, bg="green", fg="white", command=lambda: self.sprayStart())
        btnMode4 = tk.Button(frameButton, relief="solid", bd=0, image=controller.settingBtnImg, command=lambda: controller.show_frame("DistanceModePage"))
        btnMode5 = tk.Button(frameButton, relief="solid", bd=0, image=controller.settingBtnImg)

        btnMode1.place(relwidth=0.2, relheight=0.6, relx=0.1, rely=0.1)
        btnMode2.place(relwidth=0.2, relheight=0.6, relx=0.4, rely=0.1)
        btnMode3.place(relwidth=0.2, relheight=0.6, relx=0.7, rely=0.1)
        btnMode4.place(relx=0.17, rely=0.75)
        btnMode5.place(relx=0.47, rely=0.75)

    def sprayStart(self):
        if self.manualSprayOn :
            wpi.digitalWrite(4, 0)
            self.manualSprayOn = False
        else :
            wpi.digitalWrite(4, 1)
            self.manualSprayOn = True       