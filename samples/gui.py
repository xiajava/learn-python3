from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInout = Entry(self)
        self.nameInout.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInout.get() or 'world'
        messagebox.showinfo('Message', 'Hello %s' % name)


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
