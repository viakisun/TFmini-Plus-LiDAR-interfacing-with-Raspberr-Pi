from tkinter import *
from tkinter import font

class WindowDistanceMode:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1024x600")
        self.window.resizable(False, False)
        self.window.title("천연살균의학처 방역 시스템")
        self.strSprayMode = StringVar()
        self.strSprayMode.set("수동분사")
        
        #        self.window.attributes("-fullscreen",True)

        #상단메뉴
        self.labelFont = font.Font(size=12, weight="bold")
        self.frameTop = Frame(self.window, relief=RIDGE, bg="#222222", height=60)
        self.label1 = Label(self.frameTop, text="  현재 분사모드 : ", fg="white", bg="#222222", height=3, font=self.labelFont)
        self.label1.pack(side="left")
        self.lblMode = Label(self.frameTop, fg="white", bg="#222222", height=3, font=self.labelFont, textvariable=self.strSprayMode)
        self.lblMode.pack(side="left")
        self.frameTop.pack(side="top", fill=X)
        
        #왼쪽
        self.frameLeft = Frame(self.window, relief=RIDGE, bg="#c4c4c4", width = 250)
        self.frameLeft.pack(side="left",fill=Y)

        self.lblTitle = Label(self.frameLeft, fg="black", bg="#73AAEB", height=3, font=self.labelFont, text="거리인식 모드 설정")
        self.lblTitle.place(relx=0, rely=0, relwidth=1)
        
        self.imgBtnHome = PhotoImage(file='images/btn_02.gif')
        self.btnHome = Button(self.frameLeft, relief=SOLID, bd=0, image=self.imgBtnHome, bg="#c4c4c4")
        self.btnHome.place(relx=0.3, rely=0.2)

        self.imgBtnSave = PhotoImage(file='images/btn_03.gif')
        self.btnSave = Button(self.frameLeft, relief=SOLID, bd=0, image=self.imgBtnSave, bg="#c4c4c4")
        self.btnSave.place(relx=0.3, rely=0.45)

        self.imgBtnInit = PhotoImage(file='images/btn_04.gif')
        self.btnInit = Button(self.frameLeft, relief=SOLID, bd=0, image=self.imgBtnInit, bg="#c4c4c4")
        self.btnInit.place(relx=0.3, rely=0.7)


        #오른쪽
        self.frameRight = Frame(self.window, relief=RIDGE, bg="white", width = 774)
        self.frameRight.pack(side="right",fill=Y)

        #오른쪽 분사시간 조절
        self.fontContentLbl = font.Font(size=18, weight="bold")
        self.lbl01 = Label(self.frameRight, fg="black", bg="white", font=self.fontContentLbl, text="분사시간")
        self.lbl01.place(relx=0.2, rely=0.1)

        self.fontContentLbl = font.Font(size=60)
        self.lblTime = Label(self.frameRight, fg="black", bg="#c4c4c4", font=self.fontContentLbl, text="2.5", anchor="e", padx=10)
        self.lblTime.place(relx=0.2, rely=0.18, relwidth=0.3, relheight=0.23)

        self.fontContentLbl = font.Font(size=18, weight="bold")
        self.lbl02 = Label(self.frameRight, fg="black", bg="white", font=self.fontContentLbl, text="초")
        self.lbl02.place(relx=0.51, rely=0.34)

        self.fontContentButton = font.Font(size=20, weight="bold")
        self.btnTimeUp = Button(self.frameRight, text="▲", font=self.fontContentButton, relief=SOLID, bd=0, bg="#c4c4c4")
        self.btnTimeUp.place(relx=0.57, rely=0.18, relwidth=0.1, relheight=0.1)
        
        self.btnTimeDown = Button(self.frameRight, text="▼", font=self.fontContentButton, relief=SOLID, bd=0, bg="#c4c4c4")
        self.btnTimeDown.place(relx=0.57, rely=0.31, relwidth=0.1, relheight=0.1)



        #오른쪽 인식거리 조절
        self.fontContentLbl = font.Font(size=18, weight="bold")
        self.lbl03 = Label(self.frameRight, fg="black", bg="white", font=self.fontContentLbl, text="인식거리")
        self.lbl03.place(relx=0.2, rely=0.1+0.42)

        self.fontContentLbl = font.Font(size=60)
        self.lblDistance = Label(self.frameRight, fg="black", bg="#c4c4c4", font=self.fontContentLbl, text="2.5", anchor="e", padx=10)
        self.lblDistance.place(relx=0.2, rely=0.18+0.42, relwidth=0.3, relheight=0.23)

        self.fontContentLbl = font.Font(size=18, weight="bold")
        self.lbl04 = Label(self.frameRight, fg="black", bg="white", font=self.fontContentLbl, text="초")
        self.lbl04.place(relx=0.51, rely=0.34+0.42)

        self.fontContentButton = font.Font(size=20, weight="bold")
        self.btnDistanceUp = Button(self.frameRight, text="▲", font=self.fontContentButton, relief=SOLID, bd=0, bg="#c4c4c4")
        self.btnDistanceUp.place(relx=0.57, rely=0.18+0.42, relwidth=0.1, relheight=0.1)
        
        self.btnDistanceDown = Button(self.frameRight, text="▼", font=self.fontContentButton, relief=SOLID, bd=0, bg="#c4c4c4")
        self.btnDistanceDown.place(relx=0.57, rely=0.31+0.42, relwidth=0.1, relheight=0.1)

        self.window.bind("<Escape>", self.end_fullscreen)

    def windowOpen(self):
        self.window.mainloop()

    def end_fullscreen(self, event=None):
        self.window.attributes("-fullscreen", False)
        return "break"