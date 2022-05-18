# Orbits

Documentation.

_**GET_ORBIT_PARAMETERS**_

In the get_orbit_parameters function, we define the Eccentricity* and Focus parameter p.

This function gets the following parameters of orbit:

     :param v_vector: Rocket speed vector at a distance "r" from the Earth.
     :param r_vector: Rocket radius vector.
     :return: Eccentricity and "p" parameter.

To begin with, we introduce additional variables G = universal gravitational constant 6.667E-11 and Mass of the earth is , ME = 5.97e24

We calculate the gravitational parameter μ** = G*ME

We find the cross product of the vectors v and r and its length in order to calculate the focal parameter p.

Next, we find the length of the vector r and find the Eccentricity



_**GET_ORBIT_TYPE**_

The following get_orbit_type function is required to get the orbit type.

The function takes :param e: Eccentricity* and returns the orbit type (elliptical, parabolic, hyperbolic, circular, rectilinear)

-If e = 0 - circle

-If 0 < e < 1 - ellipse

-If e = 1 - parabola

-If e > 1 - hyperbola is greater than 1.

-If e = infty - a pair of lines

-If e < 0 - Exception("Incorrect value")


_**GET_TRAJECTORY**_

The get_trajectory function gets the trajectory of the conic section.

     :param p: "p" parameter in polar form of conic section.
     :param e: Eccentricity
     :return: Array of (x, y) points of trajectory.
     
The angle phi is moved in the interval from start to end with a step step, and is substituted into the following formulas: 

x = r * cos(phi), 

y = r * sin(phi), 

r = p / (1 + e * np.cos(phi))

The function returns two lists: x, y - coordinates, points of trajectory

_**USER INTERFACE**_

The program interface looks like this:
Created 2 fields for entering speed vector and radius vector, and 2 buttons: launch rocket and clear.
In order to launch a rocket, you need to enter the values of the vectors in the fields.
In order to launch a new rocket you must first press the clear button.


**_FOOTNOTE_**

*In mathematics, the eccentricity of a conic section is a non-negative real number that uniquely characterizes its shape.
More formally two conic sections are similar if and only if they have the same eccentricity.

One can think of the eccentricity as a measure of how much a conic section deviates from being circular. In particular:

-The eccentricity of a circle is zero.

-The eccentricity of an ellipse which is not a circle is greater than zero but less than 1.

-The eccentricity of a parabola is 1.

-The eccentricity of a hyperbola is greater than 1.

-The eccentricity of a pair of lines is infty


**In celestial mechanics, the standard gravitational parameter μ of a celestial body is the product of the gravitational constant G and the mass M of the bodies. For two bodies the parameter may be expressed as G(m1+m2), or as GM when one body is much larger than the other.
