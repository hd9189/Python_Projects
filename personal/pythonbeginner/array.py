from numpy import array
from numpy.core.function_base import linspace

#second word "float makes all the ints in the array a float"
x = array([1, 2, 3, 4, 5, 6.0],float)
print(x.dtype)

#creates an array, (number of lines in array, number of items in array, how many parts of array)
y = linspace(0,15,16)
print(y)