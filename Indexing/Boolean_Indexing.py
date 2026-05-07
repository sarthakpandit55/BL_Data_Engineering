import numpy as np

a = np.random.randint(1,100,24).reshape(6,4)

print(a)
print(f"Filtered array:- {a[(a>50) & (a%2 == 0)]}")