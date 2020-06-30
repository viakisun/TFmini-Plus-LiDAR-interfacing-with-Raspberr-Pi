#-*- coding:utf-8 -*-
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

class AutoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.sprayTime = controller.autoModeSprayTime
        self.sprayTimeVar = tk.StringVar()
        self.sprayTimeVar.set(str(self.sprayTime))

        self.cycleTime = controller.autoModeCycleTime
        self.cycleTimeVar = tk.StringVar()
        self.cycleTimeVar.set(str(self.cycleTime))
        
        frame = tk.Frame(self, relief="solid", bg="red", height=60)
        frame.pack(side="left", fill="both", expand=True)
        background_label = tk.Label(frame, image=controller.img03)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        btnHome = tk.Button(frame, relief="solid", bd=0, image=controller.imgBtnBack, bg="#0C4323", command=lambda: controller.show_frame("StartPage"))
        btnHome.place(relx=0.93, rely=0.03)

        #분사주기 조절
        lblCycleTime = tk.Label(frame, fg="white", bg="#467E39", font=tkfont.Font(size=50, weight="bold"), textvariable=self.cycleTimeVar, anchor="e", padx=10)
        lblCycleTime.place(relx=0.45, rely=0.36, relwidth=0.18, relheight=0.18)

        btnCycleTimeUp = tk.Button(frame, relief="solid", bd=0, command=lambda: self.upCycleTime(), image=controller.imgBtnUp, bg="#0C4323")
        btnCycleTimeUp.place(relx=0.66, rely=0.38)
        
        btnCycleTimeDown = tk.Button(frame, relief="solid", bd=0, command=lambda: self.downCycleTime(), image=controller.imgBtnDown, bg="#0C4323")
        btnCycleTimeDown.place(relx=0.76, rely=0.38)
       
        #분사시간 조절
        lblTime = tk.Label(frame, fg="white", bg="#467E39", font=tkfont.Font(size=50, weight="bold"), textvariable=self.sprayTimeVar, anchor="e", padx=10)
        lblTime.place(relx=0.45, rely=0.36 + 0.22, relwidth=0.18, relheight=0.18)

        btnTimeUp = tk.Button(frame, image=controller.imgBtnUp, relief="solid", bd=0, bg="#0C4323", command=lambda: self.upTime())
        btnTimeUp.place(relx=0.66, rely=0.38 + 0.22)
        
        btnTimeDown = tk.Button(frame, image=controller.imgBtnDown, relief="solid", bd=0, bg="#0C4323", command=lambda: self.downTime())
        btnTimeDown.place(relx=0.76, rely=0.38 + 0.22)

    def upTime(self):
        if self.controller.autoModeSprayTime < self.controller.MAX_AUTO_SPRAY_TIME :
            self.controller.autoModeSprayTime += 5
        self.sprayTimeVar.set(str(self.controller.autoModeSprayTime))

    def downTime(self):
        if self.controller.autoModeSprayTime > self.controller.MIN_AUTO_SPRAY_TIME :
            self.controller.autoModeSprayTime -= 5
        self.sprayTimeVar.set(str(self.controller.autoModeSprayTime))

    def upCycleTime(self):
        if self.controller.autoModeCycleTime < self.controller.MAX_AUTO_CYCLE_TIME :
            self.controller.autoModeCycleTime += 1
        self.cycleTimeVar.set(str(round(self.controller.autoModeCycleTime,1)))

    def downCycleTime(self):
        if self.controller.autoModeCycleTime > self.controller.MIN_AUTO_CYCLE_TIME :
            self.controller.autoModeCycleTime -= 1
        self.cycleTimeVar.set(str(round(self.controller.autoModeCycleTime,1)))