import numpy as np
import pandas as pd

data = {
    'A' : [1, 2, 3, 4,5],
    'B' : [1, 2, 3, 4, 5],
    'C' : [np.nan, 2, np.nan, 4,5],
    'D' : [1, 2, 3, 4,np.nan],
}

df = pd.DataFrame(data)

print(f"Original DataFrame:- \n{df}\n")

print(f"Data that have no nan values:- \n{df.dropna()}\n")


