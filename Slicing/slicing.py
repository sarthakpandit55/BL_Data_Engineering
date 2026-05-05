import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

# slicing 1-d array
print("Original Array:- \n", a1)
print(a1[2:8])

# slicing 2-d array
print("Original 2-d Array:- \n", a2)
print("Sliced column 2:- \n",a2[:,2])
print("Sliced row 2:- \n",a2[1,:])

print("center array:- \n", a2[1:3,1:3])
print("Extract [1, 3], [9, 11] array:- \n", a2[0:3:2, 1:4:2])

print("center array:- \n", a2[1:3,1:3])
print("Extract 4, 7  2-d array:- \n", a2[1:2, ::3])

print("center array:- \n", a2[1:3,1:3])
print("Extract [1,2,3],[5,6,7]  2-d array:- \n", a2[:2, 1::])

print("center array:- \n", a2[1:3,1:3])
print("Extract [1,3],[5,7]  2-d array:- \n", a2[:2, 1::2])


# slicing in 3-d array

print("Original Array:- \n", a3)

print("middle 2-d array:- \n", a3[1:2])
print("other then middle 2-d array:- \n", a3[::2])
print("second row of first 2-d array:- \n", a3[0,1])

print("second column of second 2-d array \n", a3[1,:,1])
print("last two value of last 2-d array \n", a3[2,2,1:])

print("extract 0,2,18,20 from 3-d array \n", a3[::2,0,::2])
