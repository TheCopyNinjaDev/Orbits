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
    pass


def get_trajectory(p: float, e: float) -> np.array:
    """
    Get trajectory of the conic section.

    :param p: "p" parameter in polar form of conic section.
    :param e: Eccentricity
    :return: Array of (x, y) points of trajectory.
    """
    pass