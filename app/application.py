import tkinter as tk
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class Application:
    def __init__(self, main_title):
        self.window = tk.Tk()
        self.window.title(main_title)
        self.window.geometry('1280x720')
        label1 = tk.Label(text="Rocket flying graph", fg="#eee", bg="#333")
        label1.pack()

        f_top = tk.LabelFrame(text="Data For Graph")

        label2 = tk.Label(f_top, text="Enter vector_r ex (1 2 3)")
        label2.pack(side=tk.TOP, expand=1)

        self.txt1 = tk.Entry(f_top, width=30)
        self.txt1.pack(side=tk.TOP, expand=1)

        label3 = tk.Label(f_top, text="Enter vector_v ex (1 2 3)")
        label3.pack(side=tk.TOP, expand=1)

        self.txt2 = tk.Entry(f_top, width=30)
        self.txt2.pack(side=tk.TOP, expand=1)
        f_top.pack(padx=10, pady=10)
        # create a figure

        self.add_button('rerender', self.print_graphics)

    def print_graphics(self):

        vector_v = self.get_vector(self.txt1.get())
        vector_r = self.get_vector(self.txt2.get())
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self.window)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self.window)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(vector_v, vector_r)
        axes.set_title('vector_v')
        axes.set_ylabel('vector_r')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    @staticmethod
    def get_vector(sting_vector):
        return np.array([int(s) for s in sting_vector.split() if s.isdigit()])

    def rerender(self):
        self.window.mainloop()

    def add_button(self, text, onclick_f):
        btn = tk.Button(self.window, text=text, command=onclick_f, bg='orange')

        btn.pack(side=tk.BOTTOM, expand=1)

