import matplotlib.pyplot as plt
import orbits


def show_trajectory(v, r):
    e, p = orbits.get_orbit_parameters(v, r)
    x, y = orbits.get_trajectory(p, e)
    plt.title(orbits.get_orbit_type(e))
    plt.plot(x, y)
    plt.show()

