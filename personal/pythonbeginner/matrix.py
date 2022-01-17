from numpy import *

arr1 = array([
				[1,2,3,5,1,5],
				[4,5,6,5,2,8]
])

print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2 = arr1.flatten()
print(arr2)

arr3 = arr2.reshape(3,4)
print(arr3)

arr4 = arr2.reshape(2,2,3)
print(arr4)

m1 = matrix('1 2 3; 4 5 6; 7 8 9')
print(m1)
print(diagonal(m1))
print(m1.min())
print(m1.max())

m2 = matrix('1 2 5; 3 4 6; 8 7 9')

m3 = m1 + m2
print(m3)

m4 = m1 * m2
print(m4)