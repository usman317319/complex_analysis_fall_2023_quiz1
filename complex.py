import numpy as np

PI = 3.14159265359

class ComplexNumber():
    def __init__(self,
                 real      : int | float,
                 imaginary : int | float
                ):
        """
        This class can be used to define complex numbers by passing real and imaginary numbers.
        The numbers are saved in tuple.

        Usuage:
        -------
            a = ComplexNumber(1, 1)\\
            a.polar_coordinates\\
            a.roots(root= 4)
        """
        self.real      = real
        self.imaginary = imaginary
        self.radius    = self.modulus()
        self.complexNumber = (real, imaginary)
    
    def modulus(self):
        """
        Consider only the positive answer.\\
        As radius is not taken negative in case of complex polar coordinates
        """
        return np.sqrt(self.real**2 + self.imaginary**2)

    @property
    def angle(self):
        """
        Returns the Angle that it makes with the x-axes.

                            |
             180-tan-1(y/x) |  tan-1(y/x)
                            |
             ---------------|---------------
                            |
             180+tan-1(y/2) |  360-tan-1(y/x)
                            |          

        """
        if self.real > 0 and self.imaginary > 0:                  # 1st Quadrant
            return np.arctan(self.imaginary/self.real)
        elif self.real < 0 and self.imaginary > 0:                # 2nd Quadrant
            return PI - (-np.arctan(self.imaginary/self.real))
        elif self.real < 0 and self.imaginary < 0:                # 3rd Quadrant
            return PI + np.arctan(self.imaginary/self.real)
        elif self.real > 0 and self.imaginary < 0:                # 4th Quadrant
            return 2*PI - (-np.arctan(self.imaginary/self.real))
        # Equal too angles to be implemented
    
    @property
    def polar_coordinates(self):
        """
        Returns Polar form of the Complex Number with format (radius, angle).
        """
        return (self.radius, self.angle)

    def roots(self, root : int):
        """
        Returns the roots of the Complex Number.

        How it works:
        -------------
            Let's take a complex number say z = 1 + ij and find it's 4th root.\\
            radius/modulus of z = sqrt(2)\\
            angle of z = PI/4 or 45 degrees\\
            z = (sqrt(2), PI/4)\\
            Finding the 4th root of z means to find number who when raised to the power of 4 give z.\\
            ---> z^(1/4) = (r, theta)\\
            ---> z = (r, theta)^(4)\\
            ---> (sqrt(2), PI/4) = (r, theta)^(4)\\
            ---> (sqrt(2), PI/4) = (r^4, 4*theta)\\
            ---> r^4 = sqrt(2) and 4*theta = PI/4 + 2*PI*k\\
            ---> r = sqrt(2)^(1/4) and theta = PI/16 + 2*PI*k/4
        """
        radius = np.power(self.radius, 1/root)
        startingAngle = self.angle/root

        roots = list()
        roots.append((radius, startingAngle))
        for i in range(1, 50):
            roots.append((radius, startingAngle + 2*PI*i/root))
        
        return roots