import numpy as np
from typing import Tuple
import math


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
    h_vector = np.int64(np.cross(v_vector, r_vector))

    # Square the elements of vector H
    h_vector_square = np.array([i ** 2 for i in h_vector], dtype=np.int64)
    # Find the sum of the elements of the vector H
    h_vector_sum = np.sum(h_vector_square, dtype=np.int64)
    # Vector length H
    h = math.sqrt(h_vector_sum)
    # Focal parameter
    p = np.int64(h**2) / MU

    # Square the elements of the vector R
    r_vector_square = np.array([i ** 2 for i in r_vector], dtype=np.int64)
    # Find the sum of the elements of the vector H
    r_vector_sum = np.sum(r_vector_square, dtype=np.int64)
    # Vector length R
    r = math.sqrt(r_vector_sum)

    # Find the vector product of vectors H and R
    vector_h_v = np.int64(np.cross(v_vector, h_vector))

    # Vector eccentricity
    e_vector = vector_h_v / MU - r_vector / r
    # Square the elements of the vector R
    e_vector_square = np.array([i ** 2 for i in e_vector], dtype=np.float64)
    # Find the sum of the elements of the vector H
    e_vector_sum = np.sum(e_vector_square, dtype=np.float64)
    # Vector length R
    e = math.sqrt(e_vector_sum)
    return e, p


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
