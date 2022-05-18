import matplotlib

matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from tkinter import *


class Application:
    def __init__(self, main_title):
        self.window = Tk()
        self.window.title(main_title)
        self.window.geometry('540x480')
        self.add_button()

    def rerender(self):
        self.window.mainloop()

    def add_button(self, text, onclick_f):
        btn = Button(self.window, text=text, command=onclick_f)
        btn.grid(column=1, row=0)

    def add_input(self):
        self.txt1 = Entry(self.window, width=10)
        self.txt1.grid(column=1, row=0)
