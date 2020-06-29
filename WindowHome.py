from tkinter import *
from tkinter import font

class WindowHome:
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
        
        #모드버튼
        self.buttonFont = font.Font(size=12, weight="bold")
        self.btnImg = PhotoImage(file='images/btn_01.png') #PhotoImage객체 생성

        self.frameButton = Frame(self.window, relief="solid", bg="white", height=60)
        self.btnMode1 = Button(self.frameButton, text="거리인식 모드", font=self.buttonFont, relief=SOLID, bd=0)
        self.btnMode2 = Button(self.frameButton, text="자동모드", font=self.buttonFont, relief=SOLID, bd=0)
        self.btnMode3 = Button(self.frameButton, text="수동분사", font=self.buttonFont, relief=SOLID, bd=2, bg="green", fg="white")
        self.btnMode4 = Button(self.frameButton, relief=SOLID, bd=0, image=self.btnImg)
        self.btnMode5 = Button(self.frameButton, relief=SOLID, bd=0, image=self.btnImg)

        self.btnMode1.place(relwidth=0.2, relheight=0.6, relx=0.1, rely=0.1)
        self.btnMode2.place(relwidth=0.2, relheight=0.6, relx=0.4, rely=0.1)
        self.btnMode3.place(relwidth=0.2, relheight=0.6, relx=0.7, rely=0.1)
        self.btnMode4.place(relx=0.17, rely=0.75)
        self.btnMode5.place(relx=0.47, rely=0.75)
        
        self.frameButton.pack(side="left", fill=BOTH, expand=True)
        

        

        self.window.mainloop()
        self.window.bind("<Escape>", self.end_fullscreen)

    def end_fullscreen(self, event=None):
        self.window.attributes("-fullscreen", False)
        return "break"