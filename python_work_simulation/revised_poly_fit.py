import numpy as np
from numpy.polynomial import polynomial as P
from matplotlib import pyplot as plt

x = np.array([0.0000, -0.0008, 0.0006, -0.002, 0.006, -0.0002, -0.001, 0.0008, -0.006,  0.004, -0.0004, 0.0002, 0.001, 0.002, -0.0006,  0.0004, -0.004, -0.008]) # Our s values go here, in order.
y = np.array([-2.9961, -3.214,  -2.8877, -3.764, -2.089,  -3.0731, -3.321, -2.8176, -5.699, -2.266, -3.1439,  -2.9393, -2.727, -2.535,  -3.2055, -2.9062, -4.686, -6.523]) # Our values for log_10(probability of fixation) go here.

output1 = P.polyfit(x,y,3,full=False) # to the 3rd order
output2 = P.polyfit(x,y,4,full=False) # to the 4th order
output3 = P.polyfit(x,y,5,full=False) # to the 5th order


def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y

plt.plot(x,y,'ro')
p = np.linspace(-0.008, 0.006, 50)
plt.plot(p, PolyCoefficients(p, output1)) # 3rd order graph
plt.show()

plt.plot(x,y,'ro')
plt.plot(p, PolyCoefficients(p, output2)) #4th order graph
plt.show()

plt.plot(x,y,'ro')
plt.plot(p, PolyCoefficients(p, output3)) #5th order graph
plt.show()


print(f'# Coefficients for 3rd order poly_fit graph:', output1)
print(f'# Coefficients for 4th order poly_fit graph:', output2)
print(f'# Coefficients for 5th order poly_fit graph:', output3)
