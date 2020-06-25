from tkinter import *
from RangeFinder import *

_root = Tk()

class SprayManagerWindow:
    def __init__(self):
        _root.geometry("800x600")
        _root.attributes("-fullscreen",True)
        _root.bind("<Escape>", self.end_fullscreen)
        self.frame = Frame(_root, width=1280, height=800, relief='solid',bd=1)
        self.frame.place(x=10, y=10)
        self.distanceVar = StringVar()
        self.distanceVar.set("Show me distance")

        label_distance = Label(self.frame, textvariable=self.distanceVar, relief=RAISED)
        label_distance.pack()

        #디버그용도로 사용하는 라벨을 위한 세팅
        self.debugVar = StringVar()
        self.debugVar.set("Debug Message")
        label_debug = Label(_root, textvariable=self.debugVar)
        label_debug.place(x=700,y=300)
        label_debug.pack()

        button = Button(self.frame, overrelief="solid", width=15, command=self.update, repeatdelay=1000, repeatinterval=100, text="버튼")
        button.pack()

        self.rangeFinder = RangeFinder()

    def refresher(self):
        distance = self.rangeFinder.read()
        output = str(distance)
        self.distanceVar.set(output)
        _root.after(10, self.refresher) # every second...

    def start(self):
        return

    def stop(self):
        return

    def update(self):
        return

    def unload(self):
        _root.mainloop()

    def end_fullscreen(self, event=None):
        _root.attributes("-fullscreen", False)
        return "break"

_manager = SprayManagerWindow()
_manager.refresher()

_root.mainloop()