from tkinter import *


class Application:
    def __init__(self, main_title):
        self.window = Tk()
        self.window.title(main_title)
        self.window.geometry('540x480')
        self.add_button()

    def rerender(self):
        self.window.mainloop()

    def add_button(self):
        btn = Button(self.window, text="Не нажимать!")
        btn.grid(column=1, row=0)
