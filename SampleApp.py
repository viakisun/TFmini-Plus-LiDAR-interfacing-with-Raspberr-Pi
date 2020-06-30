import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from StartPage import *
from PageOne import *
from PageTwo import *
from DistanceModePage import *
from SprayMode import *

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #폰트설정
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.modebutton_font = tkfont.Font(size=12, weight="bold")
        self.label_font_01 = tkfont.Font(size=12, weight="bold")
        self.label_font_02 = tkfont.Font(size=18, weight="bold")
        self.label_font_03 = tkfont.Font(size=60)
        self.label_font_04 = tkfont.Font(size=20)

        #이미지 관리
        self.settingBtnImg = tk.PhotoImage(file='images/btn_01.png') #PhotoImage객체 생성
        self.imgBtnHome = tk.PhotoImage(file='images/btn_02.gif')
        self.imgBtnSave = tk.PhotoImage(file='images/btn_03.gif')
        self.imgBtnInit = tk.PhotoImage(file='images/btn_04.gif')

        #기본값 관리
        self.sprayMode = SprayMode.MANUAL

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.attributes()

        self.frames = {}
        for F in (StartPage, DistanceModePage, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def getSprayModeStr(self):
        if self.sprayMode == SprayMode.DISTANCE :
            return "거리인식 모드"
        elif self.sprayMode == SprayMode.AUTO :
            return "자동 모드"
        elif self.sprayMode == SprayMode.MANUAL :
            return "수동분사"
        else :
            return False

    def setSprayMode(self, sprayMode):
        self.sprayMode = sprayMode

if __name__ == "__main__":
    app = SampleApp()
    app.title("천연살균의학처 방역 시스템")
    app.geometry("1024x600")
    app.attributes("-fullscreen",True)
    app.resizable(False, False)
    app.mainloop()