import numpy as np

from typing import Tuple


def get_orbit_parameters(v: np.array, r: np.array) -> Tuple[float, float]:
    """
    Get parameters of orbit.

    :param v: Rocket speed vector at a distance "r" from the Earth.
    :param r: Rocket radius vector.
    :return: Eccentricity and "p" parameter.
    """
    pass


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
