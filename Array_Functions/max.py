import numpy as np

a = np.array([[1,21,34],[43,99,23], [72,84,9]])
print("original Array:- ", a)
print("Max of array:- ", np.max(a, axis = 0))