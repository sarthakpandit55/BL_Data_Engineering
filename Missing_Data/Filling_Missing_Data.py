import pandas as pd
import numpy as np

data = {
    'A' : [1, 2, np.nan, 4,5],
    'B' : [1, 2, 3,np.nan,5],
    'C' : [np.nan, 2, np.nan, 4,5],
    'D' : [1, 2, 3, 4,np.nan],
}

df = pd.DataFrame(data)

print(f"Original Data:- \n{df}")

print(f"Filled Data:- \n{df.fillna(0)}")

values = {"A": 100, "B": 200, "C": 300, "D": 400}
print(f"Filled Data using given values:- \n{df.fillna(value=values)}")
