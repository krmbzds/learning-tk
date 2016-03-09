from tkinter import *

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack()
        self.var = BooleanVar()
        checkbox = Checkbutton(self, text="Show title", variable=self.var, command=self.onClick)
        checkbox.pack()

    def onClick(self):
        if self.var.get() == True:
            self.parent.title("Checkbutton")
        else:
            self.parent.title("")

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

main()
