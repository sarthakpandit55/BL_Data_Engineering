import numpy as np

a = np.array([1,2,3,4])
print(a)

# 2d array
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"\n 2-d array:-  {b}")

# 3d array

c = np.array([[[1,2], [3,4]],[[5,6], [7,8]],[[9,10], [11,12]]])
print(f"\n 3-d array:-  {c}")


# arange() function
d = np.arange(1,11)
print(f"\n{d}")

# .linspace()

e = np.linspace(1,10,5)
print(f"\n{e}")