import tkinter as tk                # python 3

class DistanceModePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.strSprayMode = tk.StringVar()
        self.strSprayMode.set("수동분사")
        
        #상단메뉴
        frameTop = tk.Frame(self, relief="solid", bg="#222222", height=60)
        frameTop.pack(side="top", fill="x")
        label1 = tk.Label(frameTop, text="  현재 분사모드 : ", fg="white", bg="#222222", height=3)
        label1.pack(side="left")
        lblMode = tk.Label(frameTop, fg="white", bg="#222222", height=3, textvariable=self.strSprayMode)
        lblMode.pack(side="left")
        
        #왼쪽
        frameLeft = tk.Frame(self, relief="solid", bg="#c4c4c4", width = 250)
        frameLeft.pack(side="left",fill="y")

        lblTitle = tk.Label(frameLeft, fg="black", bg="#73AAEB", height=3, font=controller.label_font_01, text="거리인식 모드 설정")
        lblTitle.place(relx=0, rely=0, relwidth=1)
        
        btnHome = tk.Button(frameLeft, relief="solid", bd=0, image=controller.imgBtnHome, bg="#c4c4c4", command=lambda: controller.show_frame("StartPage"))
        btnHome.place(relx=0.3, rely=0.2)
       
        btnSave = tk.Button(frameLeft, relief="solid", bd=0, image=controller.imgBtnSave, bg="#c4c4c4")
        btnSave.place(relx=0.3, rely=0.45)

        btnInit = tk.Button(frameLeft, relief="solid", bd=0, image=controller.imgBtnInit, bg="#c4c4c4")
        btnInit.place(relx=0.3, rely=0.7)


        #오른쪽
        frameRight = tk.Frame(self, relief="solid", bg="white", width = 774)
        frameRight.pack(side="right",fill="y")

        #오른쪽 분사시간 조절
        lbl01 = tk.Label(frameRight, fg="black", bg="white", font=controller.label_font_02, text="분사시간")
        lbl01.place(relx=0.2, rely=0.1)

        lblTime = tk.Label(frameRight, fg="black", bg="#c4c4c4", font=controller.label_font_03, text="2.5", anchor="e", padx=10)
        lblTime.place(relx=0.2, rely=0.18, relwidth=0.3, relheight=0.23)

        lbl02 = tk.Label(frameRight, fg="black", bg="white", font=controller.label_font_02, text="초")
        lbl02.place(relx=0.51, rely=0.34)

        btnTimeUp = tk.Button(frameRight, text="▲", font=controller.label_font_04, relief="solid", bd=0, bg="#c4c4c4")
        btnTimeUp.place(relx=0.57, rely=0.18, relwidth=0.1, relheight=0.1)
        
        btnTimeDown = tk.Button(frameRight, text="▼", font=controller.label_font_04, relief="solid", bd=0, bg="#c4c4c4")
        btnTimeDown.place(relx=0.57, rely=0.31, relwidth=0.1, relheight=0.1)



        #오른쪽 인식거리 조절
        lbl03 = tk.Label(frameRight, fg="black", bg="white", font=controller.label_font_02, text="인식거리")
        lbl03.place(relx=0.2, rely=0.1+0.42)

        lblDistance = tk.Label(frameRight, fg="black", bg="#c4c4c4", font=controller.label_font_03, text="2.5", anchor="e", padx=10)
        lblDistance.place(relx=0.2, rely=0.18+0.42, relwidth=0.3, relheight=0.23)

        lbl04 = tk.Label(frameRight, fg="black", bg="white", font=controller.label_font_02, text="m")
        lbl04.place(relx=0.51, rely=0.34+0.42)

        btnDistanceUp = tk.Button(frameRight, text="▲", font=controller.label_font_04, relief="solid", bd=0, bg="#c4c4c4")
        btnDistanceUp.place(relx=0.57, rely=0.18+0.42, relwidth=0.1, relheight=0.1)
        
        btnDistanceDown = tk.Button(frameRight, text="▼", font=controller.label_font_04, relief="solid", bd=0, bg="#c4c4c4")
        btnDistanceDown.place(relx=0.57, rely=0.31+0.42, relwidth=0.1, relheight=0.1)