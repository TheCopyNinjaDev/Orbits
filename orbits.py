import numpy as np

from typing import Tuple


def get_orbit_parameters(v_vector: np.array, r_vector: np.array) -> Tuple[float, float]:
    """
    Get parameters of orbit.

    :param v_vector: Rocket speed vector at a distance "r" from the Earth.
    :param r_vector: Rocket radius vector.
    :return: Eccentricity and "p" parameter.
    """
    """ Realized by Alexei Zolotarev """
    # Enter additional variables
    G = 6.667e-11
    ME = 5.97e24
    # mu coefficient
    MU = G * ME
    # Vector H
    h_vector = np.cross(v_vector, r_vector)
    # Vector length H
    h = np.sum([i**2 for i in h_vector])**(1/2)
    # Focal parameter
    p = h**2 / MU
    # Vector length R
    r = np.sum([i**2 for i in r_vector])**(1/2)
    # Vector eccentricity
    e_vector = np.cross(v_vector, h_vector) / MU - r_vector / r
    # Vector length eccentricity
    e = np.sum([i**2 for i in e_vector])**(1/2)
    return e, p


def get_orbit_type(e: float) -> str:
    """
    Get type of orbit.

    :param e: Eccentricity
    :return: Type of orbit (elliptical, parabolic, hyperbolic, circular, rectilinear).
    """
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


def get_trajectory(p: float, e: float) -> np.array:
    """
    Get trajectory of the conic section.

    :param p: "p" parameter in polar form of conic section.
    :param e: Eccentricity
    :return: Array of (x, y) points of trajectory.
    """
    pass
