import numpy as np

from typing import Tuple


def get_orbit_parameters(v_vector: np.array, r_vector: np.array) -> Tuple[float, float]:
    # Enter additional variables
    G = 6.667e-11
    ME = 5.97e24
    # mu coefficient
    MU = G * ME

    try:
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

        if np.isnan(e) or np.isnan(p):
            raise Exception
        else:
            return e,p
    except Exception:
        return "Incorrect Data"
    except ArithmeticError:
        return "Arithmetic error"
    except TypeError:
        return "An operation or function is applied to an invalid type value"


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
