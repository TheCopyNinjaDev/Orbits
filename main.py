# -*- coding: utf-8 -*-
from application import *
import numpy as np
from Vizualization import show_trajectory


if __name__ == '__main__':
    app = App()
    app.mainloop()


vector_v = input()
vector_v = np.array([int(s) for s in vector_v.split() if s.isdigit()])

vector_r = input()
vector_r = np.array([int(s) for s in vector_r.split() if s.isdigit()])
