import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

print(a1[-1])
print(a2[1,0])
print(a3[1,1,0])