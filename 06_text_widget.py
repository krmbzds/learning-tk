from tkinter import *

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack()
        text = Text(self)
        text.insert(INSERT, 'Hello')
        text.insert(END, 'Bye bye')
        text.pack()
        text.tag_add('Here', '1.0', '1.4')
        text.tag_add('Start', '1.8', '1.13')
        text.tag_config('Here', background='yellow', foreground='blue')
        text.tag_config('Start', background='black', foreground='green')

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
