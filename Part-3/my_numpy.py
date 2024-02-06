#import numpy
import numpy as np
a = np.array([1,2,3,4,5])
print(a)

#data type parameter
a = np.array([1, 2, 3, 4, 5], dtype = float)
print(a)

#shape function
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

#2D Array
a = np.array([[1,2], [3,4], [5,6]])
print (a)

#3D Array
a = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[10,11,12]],
              [[13,14,15],[16,17,18]],
              [[19,20,21],[22,23,24]]])

print(a[2])
print(a[2][1])
print(a[2][1][2])

x = np.zeros([10,5], dtype = int)
print(x)

x = np.ones([10,5], dtype = int)
print(x)

x = np.linspace(10,20,5)
print(x)

#array manipulation
a = np.array([10,20,30,40,50])
b = np.array([2,3,4,5,6])

c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
c = a * 2
print(c)
c = a * 2 + 5
print(c)
c = b ** 2
print(c)

#spesific functions
y = np.array([10,20,30,40,50])
print(y.sum())
print(y.min())
print(y.max())
print(y.mean())