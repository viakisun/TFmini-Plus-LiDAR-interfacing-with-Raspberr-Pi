#-*- coding:utf-8 -*-
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

class DistanceModePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.sprayTime = controller.distanceModeSprayTime
        self.sprayTimeVar = tk.StringVar()
        self.sprayTimeVar.set(str(self.sprayTime))

        self.detectDistance = controller.distanceModeDetectDistance
        self.detectDistanceVar = tk.StringVar()
        self.detectDistanceVar.set(str(self.detectDistance))
        
        frame = tk.Frame(self, relief="solid", bg="red", height=60)
        frame.pack(side="left", fill="both", expand=True)
        background_label = tk.Label(frame, image=controller.imgBgDetect)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        btnHome = tk.Button(frame, relief="solid", bd=0, image=controller.imgBtnBack, bg="#0C4323", command=lambda: controller.show_frame("StartPage"))
        btnHome.place(relx=0.93, rely=0.03)

        #인식거리 조절
        lblDistance = tk.Label(frame, fg="white", bg="#467E39", font=tkfont.Font(size=50, weight="bold"), textvariable=self.detectDistanceVar, anchor="e", padx=10)
        lblDistance.place(relx=0.45, rely=0.36, relwidth=0.18, relheight=0.18)

        btnDistanceUp = tk.Button(frame, relief="solid", bd=0, command=lambda: self.upDistance(), image=controller.imgBtnUp, bg="#0C4323")
        btnDistanceUp.place(relx=0.66, rely=0.38)
        
        btnDistanceDown = tk.Button(frame, relief="solid", bd=0, command=lambda: self.downDistance(), image=controller.imgBtnDown, bg="#0C4323")
        btnDistanceDown.place(relx=0.76, rely=0.38)
       
        #오른쪽 분사시간 조절
        lblTime = tk.Label(frame, fg="white", bg="#467E39", font=tkfont.Font(size=50, weight="bold"), textvariable=self.sprayTimeVar, anchor="e", padx=10)
        lblTime.place(relx=0.45, rely=0.36 + 0.22, relwidth=0.18, relheight=0.18)

        btnTimeUp = tk.Button(frame, image=controller.imgBtnUp, relief="solid", bd=0, bg="#0C4323", command=lambda: self.upTime())
        btnTimeUp.place(relx=0.66, rely=0.38 + 0.22)
        
        btnTimeDown = tk.Button(frame, image=controller.imgBtnDown, relief="solid", bd=0, bg="#0C4323", command=lambda: self.downTime())
        btnTimeDown.place(relx=0.76, rely=0.38 + 0.22)

    def upTime(self):
        if self.controller.distanceModeSprayTime < self.controller.MAX_SPRAY_TIME :
            self.controller.distanceModeSprayTime += 0.5
        self.sprayTimeVar.set(str(self.controller.distanceModeSprayTime))

    def downTime(self):
        if self.controller.distanceModeSprayTime > self.controller.MIN_SPRAY_TIME :
            self.controller.distanceModeSprayTime -= 0.5
        self.sprayTimeVar.set(str(self.controller.distanceModeSprayTime))

    def upDistance(self):
        if self.controller.distanceModeDetectDistance < self.controller.MAX_DETECT_DISTANCE :
            self.controller.distanceModeDetectDistance += 0.1
        self.detectDistanceVar.set(str(round(self.controller.distanceModeDetectDistance,1)))

    def downDistance(self):
        if self.controller.distanceModeDetectDistance > self.controller.MIN_DETECT_DISTANCE :
            self.controller.distanceModeDetectDistance -= 0.1
        self.detectDistanceVar.set(str(round(self.controller.distanceModeDetectDistance,1))) 