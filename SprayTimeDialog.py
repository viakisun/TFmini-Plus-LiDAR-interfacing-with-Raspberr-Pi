class SprayTimeDialog:
    def __init__(self, parent):
        title = "분사시간"
        labeltext = "분사시간을 입력하세요."

        #valor = StringVar()
        #valor.set("Hola Manejando datos")

        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        if len(title) > 0: self.top.title(title)
        if len(labeltext) == 0: labeltext = 'Valor'
        Label(self.top, text=labeltext).pack()
        self.top.bind("<Return>", self.ok)
        #self.e = Entry(self.top, text=valor.get())
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