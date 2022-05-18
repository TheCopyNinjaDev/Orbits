import numpy as np
from Vizualization import show_trajectory

vector_v = input()
vector_v = np.array([int(s) for s in vector_v.split() if s.isdigit()])

vector_r = input()
vector_r = np.array([int(s) for s in vector_r.split() if s.isdigit()])

try:
    show_trajectory(vector_v, vector_r)
except Exception:
    raise ValueError("Invalid Values")