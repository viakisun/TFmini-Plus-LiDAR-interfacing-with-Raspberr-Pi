from tkinter import *
from RangeFinder import *

_root = Tk()

class SprayManagerWindow:
    def __init__(self):
        self.frame = Frame(_root, width=1280, height=800, relief='solid',bd=1)
        self.frame.place(x=10, y=10)

        self.distanceVar = StringVar()
        self.distanceVar.set("Show me distance")

        label_distance = Label(self.frame, textvariable=self.distanceVar, relief=RAISED)
        label_distance.pack()

        button = Button(self.frame, overrelief="solid", width=15, command=self.update, repeatdelay=1000, repeatinterval=100)
        button.pack()

        self.rangeFinder = RangeFinder()

    def refresher(self):
        distance = self.rangeFinder.read()
        output = str(distance)
        self.distanceVar.set(output)
        _root.after(10, refresher) # every second...

    def start(self):
        return

    def stop(self):
        return

    def update(self):
        return

    def unload(self):
        _root.mainloop()

_manager = SprayManagerWindow()
_manager.refresher()

_root.mainloop()