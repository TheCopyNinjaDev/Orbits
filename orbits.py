import numpy as np

from typing import Tuple


def get_orbit_parameters(v: np.array, r: np.array) -> Tuple[float, float]:
    """
    Get parameters of orbit.

    :param v: Rocket speed vector at a distance "r" from the Earth.
    :param r: Rocket radius vector.
    :return: Eccentricity and "p" parameter.
    """
    """ Realized by Alexei Zolotarev """
    # Enter additional variables
    g = 6.667e-11
    me = 5.97e24

    # gravitational parameter mu
    mu = g * me

    # Vector H
    h_vector = np.cross(v, r)

    # Vector length H
    h = np.sum([i**2 for i in h_vector])**(1/2)

    # Focal parameter
    p = h**2 / mu

    # Vector length R
    r = np.sum([i**2 for i in r])**(1/2)

    # Vector eccentricity
    e_vector = np.cross(v, h_vector) / mu - r / r

    # Vector length eccentricity
    e = np.sum([i**2 for i in e_vector])**(1/2)

    return e, p


def get_orbit_type(e: float) -> str:
    """
    Get type of orbit.

    :param e: Eccentricity
    :return: Type of orbit (elliptical, parabolic, hyperbolic, circular, rectilinear).
    """
    """ Realized by Denis Arkhipov """
    if e == 0:
        return "circular"
    elif 0 < e < 1:
        return "elliptical"
    elif e == 1:
        return "parabolic"
    elif 1 < e < float('inf'):
        return "hyperbolic"
    elif e == float('inf'):
        return "rectilinear"
    elif e <= 0:
        raise Exception("Incorrect value")


def get_trajectory(p: float, e: float, start: float = 0, end: float = 2 * pi, step: float = 0.005):
    """
    Get trajectory of the conic section.
    
    :param p: "p" parameter in polar form of conic section.
    :param e: Eccentricity.
    :param start: first value of a range of phi (angles) values.
    :param end: last value of a range of phi (angles) values.
    :return: Array of (x, y) points of trajectory.
    """
    x = []
    y = []

    # array of angles in radian
    phi_arr = np.arange(start, end, step)

    for phi in phi_arr:

        r = p / (1 + e * math.cos(phi))

        x.append(r * math.cos(phi))
        y.append(r * math.sin(phi))
    
    return x, y
