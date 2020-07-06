#-*- coding:utf-8 -*-

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from startpage import *
from DistanceModePage import *
from ManualPage import *
from AutoPage import *
from SprayMode import *

class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # test code
        config = ConfigManager()

        print(config.detect_spray_duration_sec)

        print(config.get_value("detect_spray_duration_sec"))
        config.set_value("detect_spray_duration_sec", 5)
        print(config.get_value("detect_spray_duration_sec"))

        #이미지 관리
        self.settingBtnImg = tk.PhotoImage(file='images/btn_01.png') #PhotoImage객체 생성
        self.imgBgEmpty = tk.PhotoImage(file='images/bg_empty.png')
        self.imgBgDetect = tk.PhotoImage(file='images/bg_detect.png')
        self.imgBgAuto = tk.PhotoImage(file='images/bg_auto.png')
        self.imgBgManual = tk.PhotoImage(file='images/bg_manual.png')

        self.imgBtnDistance01 = tk.PhotoImage(file='images/btnDistance01.png')
        self.imgBtnDistance02 = tk.PhotoImage(file='images/btnDistance02.png')
        self.imgBtnAuto01 = tk.PhotoImage(file='images/btnAuto01.png')
        self.imgBtnAuto02 = tk.PhotoImage(file='images/btnAuto02.png')
        self.imgBtnManual01 = tk.PhotoImage(file='images/btnManual01.png')
        self.imgBtnManual02 = tk.PhotoImage(file='images/btnManual02.png')
        self.imgBtnBack = tk.PhotoImage(file='images/btnBack.png')
        self.imgBtnUp = tk.PhotoImage(file='images/btnUp.png')
        self.imgBtnDown = tk.PhotoImage(file='images/btnDown.png')

        self.sprayMode = SprayMode.MANUAL

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.config(cursor="none")
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
    app = MainApp()
    app.title("천연살균의학처 방역 시스템")
    app.geometry("1024x600")
    app.attributes("-fullscreen",True)
    app.resizable(False, False)
    app.mainloop()