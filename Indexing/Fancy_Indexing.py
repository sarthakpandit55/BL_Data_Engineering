import numpy as np

a = np.arange(24).reshape(6,4)
print(a)
print(f"Indexed array: {a[[2,4,5],[1,3,2]]}")

# np.ix_()
print(f"Indexed array: {a[np.ix_([2,4,5],[1,3])]}")