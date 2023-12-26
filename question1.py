import numpy as np
from complex import ComplexNumber

# Q1 Solution

number = ComplexNumber(real= -4, imaginary= np.sqrt(1))
# 50 Roots of complex number -1 + 3^1/2 are
print(number.roots(root= 4))
