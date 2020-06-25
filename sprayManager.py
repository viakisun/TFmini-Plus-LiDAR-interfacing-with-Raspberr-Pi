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

        button = Button(self.frame, overrelief="solid", width=15, command=self.openSprayDialog, repeatdelay=1000, repeatinterval=100, text="버튼")
        button.pack()

        self.rangeFinder = RangeFinder()

    def refresher(self):
        distance = self.rangeFinder.read()
        #output = str(distance)
        #self.distanceVar.set(output)
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

    def openSprayDialog(self):
        d = SprayTimeDialog(_root, self.valor, "Probando Dialogo", "Dame valor")
        _root.wait_window(d.top)
        #self.valor.set(d.ejemplo)


class SprayTimeDialog:
    def __init__(self, parent, valor, title, labeltext = '' ):
        self.valor = valor
 
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        if len(title) > 0: self.top.title(title)
        if len(labeltext) == 0: labeltext = 'Valor'
        Label(self.top, text=labeltext).pack()
        self.top.bind("<Return>", self.ok)
        self.e = Entry(self.top, text=valor.get())
        self.e.bind("<Return>", self.ok)
        self.e.bind("<Escape>", self.cancel)
        self.e.pack(padx=15)
        self.e.focus_set()
        b = Button(self.top, text="OK", command=self.ok)
        b.pack(pady=5)
 
    def ok(self, event=None):
        print("Has escrito ...", self.e.get())
        self.valor.set(self.e.get())
        self.top.destroy()
 
    def cancel(self, event=None):
        self.top.destroy()

_manager = SprayManagerWindow()
_manager.refresher()

_root.mainloop()