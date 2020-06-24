from tkinter import *
from RangerFinder import *

root = tk.Tk()

class SprayManagerWindow:
    def __init__(self):
        global root

        self.frame = Frame(root, width=1280, height=800, relief='solid',bd=1)
        self.frame.place(x=10, y=10)

        self.label_distance = Label(frame, textvariable=distanceVar, relief=RAISED)
        self.distanceBar = StringVar()
        self.distanceVar.set("Show me distance")
        self.label_distance.pack()

        self.button = Button(window, overrelief="solid", width=15, command=self.Update, repeatdelay=1000, repeatinterval=100)
        self.button.pack()

        self.rangeFinder = RangerFinder()

    def refresher(self):
        distance = self.rangeFinder.read()
        output = str(distance)
        self.distanceVar.set(output)
        self.root.after(10, refresher) # every second...

    def start(self):
        self.rangeFinder.start();

    def stop(self):

    def unload(self):
        self.root.mainloop()

manager = SprayManagerWindow()
manager.refresher()

root.mainloop()