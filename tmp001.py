from tkinter import *
class Application():
    def __init__(self):
        self.root = Tk()
        Label(self.root, text='Object-style application').pack()
        Button(self.root, text='Quit', command=root.destroy).pack()
        self.root.mainloop()
if __name__ == '__main__':
    Application()
