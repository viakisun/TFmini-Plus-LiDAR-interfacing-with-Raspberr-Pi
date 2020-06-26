from tkinter import *

class SprayTimeDialog():
    m_title = "분사시간"
    m_labeltext = "분사시간을 입력하세요."

    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        if len(m_title) > 0: self.top.title(m_title)
        if len(m_labeltext) == 0: m_labeltext = 'Valor'
        Label(self.top, text=m_labeltext).pack()
        self.top.bind("<Return>", self.ok)
        self.e = Entry(self.top)
        self.e.bind("<Return>", self.ok)
        self.e.bind("<Escape>", self.cancel)
        self.e.pack(padx=15)
        self.e.focus_set()
        b = Button(self.top, text="OK", command=self.ok)
        b.pack(pady=5)
 
    def ok(self, event=None):
        print("Has escrito ...", self.e.get())
        valor.set(self.e.get())
        self.top.destroy()
 
    def cancel(self, event=None):
        self.top.destroy()