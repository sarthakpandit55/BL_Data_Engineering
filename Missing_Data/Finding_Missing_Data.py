import pandas as pd
import numpy as np

data = {
    'A' : [1, 2, np.nan, 4,5],
    'B' : [1, 2, 3,np.nan,5],
    'C' : [np.nan, 2, np.nan, 4,5],
    'D' : [1, 2, 3, 4,np.nan],
}

df = pd.DataFrame(data)
print(f"Original Dataframe:- \n{df}\n")

print(f"Missing Data :- \n{df.isna()}\n")
print(f"Total Missing Data in each row :- \n{df.isna().sum()} \n")