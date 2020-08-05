import tkinter as tk
import platform
from config_value import ConfigValue

if platform.system() == "Linux" :
    import RPi.GPIO as GPIO

class SettingPage(tk.Frame):
    def __init__(self, parent, controller, background_img):
        tk.Frame.__init__(self, parent)
        self.COLOR_BUTTON_BACKGROUND = "#0C4323"
        self.controller = controller
        
        self.frame = tk.Frame(self, relief="solid", height=60)
        self.frame.pack(side="left", fill="both", expand=True)

        self.bg_image = background_img

        background_label = tk.Label(self.frame, image=self.bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.imgBtnBack = tk.PhotoImage(file='/home/pi/devwork/nsc/nsc_rc/images/btnBack.png')
        self.btnHome = tk.Button(self.frame, relief="solid", bd=0, highlightthickness=0, image=controller.imgBtnBack, bg=self.COLOR_BUTTON_BACKGROUND, command=lambda: self.go_start_page())

        self.imgBtnUp = tk.PhotoImage(file='/home/pi/devwork/nsc/nsc_rc/images/btnUp.png')
        self.imgBtnDown = tk.PhotoImage(file='/home/pi/devwork/nsc/nsc_rc/images/btnDown.png')

        if platform.system() == "Linux" :
            GPIO.setmode(GPIO.BCM)

    def is_linux_system(self):
        if platform.system() == "Linux" :
            return True
        return False

    def go_start_page(self):
        if platform.system() == "Linux" :
            GPIO.output(ConfigValue.SPRAY_WPI_NUM,False)
        self.controller.show_frame("StartPage")
