#-*- coding:utf-8 -*-

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from start_page import StartPage
from detect_page import *
from manual_page import *
from auto_page import AutoPage
from spray_mode import *
from config_value import ConfigValue

class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #이미지 관리
        imgBgEmpty = tk.PhotoImage(file='/home/pi/devwork/nsc/nsc_rc/images/bg_empty.png')
        imgBgDetect = tk.PhotoImage(file='/home/pi/devwork/nsc/nsc_rc/images/bg_detect.png')
        imgBgAuto = tk.PhotoImage(file='/home/pi/devwork/nsc/nsc_rc/images/bg_auto.png')
        imgBgManual = tk.PhotoImage(file='/home/pi/devwork/nsc/nsc_rc/images/bg_manual.png')
        self.imgBtnBack = tk.PhotoImage(file='/home/pi/devwork/nsc/nsc_rc/images/btnBack.png')

        if platform.system() == "Linux":
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(ConfigValue.SPRAY_WPI_NUM, GPIO.OUT)
        
        self.sprayMode = SprayMode.MANUAL

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        if platform.system() == "Linux":
            container.config(cursor="none")

        self.attributes()

        self.frames = {}
        for F in (StartPage, DetectPage, ManualPage, AutoPage):
            page_name = F.__name__
            if F == StartPage:
                bg_img = imgBgEmpty
            elif F == DetectPage:
                bg_img = imgBgDetect                
            elif F == ManualPage:
                bg_img = imgBgManual
            elif F == AutoPage:
                bg_img = imgBgAuto

            frame = F(parent=container, controller=self, background_img=bg_img)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        if page_name == 'ManualPage':
            frame.spray_on_check = False
            frame.init_spray()
            frame.change_spray_btn()

        frame.tkraise()

    def setSprayMode(self, sprayMode):
        self.sprayMode = sprayMode

if __name__ == "__main__":
    app = MainApp()
    app.title("천연살균의학처 방역 시스템")
    app.geometry("1024x600")
    
    if platform.system() == "Linux":
        app.attributes("-fullscreen",True)
        
    app.resizable(False, False)
    app.mainloop()