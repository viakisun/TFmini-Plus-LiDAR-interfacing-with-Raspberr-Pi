#-*- coding:utf-8 -*-

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from StartPage import *
from DistanceModePage import *
from ManualPage import *
from AutoPage import *
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
        self.img01 = tk.PhotoImage(file='images/bg_01.png')
        self.img02 = tk.PhotoImage(file='images/bg_02.png')
        self.img03 = tk.PhotoImage(file='images/bg_03.png')
        self.img04 = tk.PhotoImage(file='images/bg_04.png')

        self.imgBtnDistance01 = tk.PhotoImage(file='images/btnDistance01.png')
        self.imgBtnDistance02 = tk.PhotoImage(file='images/btnDistance02.png')
        self.imgBtnAuto01 = tk.PhotoImage(file='images/btnAuto01.png')
        self.imgBtnAuto02 = tk.PhotoImage(file='images/btnAuto02.png')
        self.imgBtnManual01 = tk.PhotoImage(file='images/btnManual01.png')
        self.imgBtnManual02 = tk.PhotoImage(file='images/btnManual02.png')
        self.imgBtnBack = tk.PhotoImage(file='images/btnBack.png')
        self.imgBtnUp = tk.PhotoImage(file='images/btnUp.png')
        self.imgBtnDown = tk.PhotoImage(file='images/btnDown.png')
        self.imgBtnSprayOn = tk.PhotoImage(file='images/btnSprayOn.png')
        self.imgBtnSprayOff = tk.PhotoImage(file='images/btnSprayOff.png')


        #기본값 관리
        self.sprayMode = SprayMode.MANUAL
        self.distanceModeSprayTime = 5.5
        self.distanceModeDetectDistance = 1.0
        self.MAX_SPRAY_TIME = 10.0
        self.MIN_SPRAY_TIME = 1.0
        self.MAX_DETECT_DISTANCE = 3.0
        self.MIN_DETECT_DISTANCE = 0.5

        self.distanceModeSprayTime = 5.5
        self.distanceModeDetectDistance = 1.0

        


        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.attributes()

        self.frames = {}
        for F in (StartPage, DistanceModePage, AutoPage, ManualPage):
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

    def setSprayMode(self, sprayMode):
        self.sprayMode = sprayMode

if __name__ == "__main__":
    app = SampleApp()
    app.title("천연살균의학처 방역 시스템")
    app.geometry("1024x600")
    # app.attributes("-fullscreen",True)
    app.resizable(False, False)
    app.mainloop()