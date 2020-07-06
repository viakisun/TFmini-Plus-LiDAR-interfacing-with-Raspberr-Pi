import tkinter as tk
import platform

if platform.system() == "Linux" :
    import odroid_wiringpi as wpi

class SettingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        frame = tk.Frame(self, relief="solid", bg="red", height=60)
        frame.pack(side="left", fill="both", expand=True)
        background_label = tk.Label(frame, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        btnHome = tk.Button(frame, relief="solid", bd=0, image=controller.imgBtnBack, bg="#0C4323", command=lambda: controller.show_frame("StartPage"))
        btnHome.place(relx=0.93, rely=0.03)

    def is_linux_system(self):
        if platform.system() == "Linux" :
            return True

        return False