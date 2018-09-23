import pandas as pd
import numpy as np


s1 = pd.Series([0, 1, 2, 3])
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5])
d = pd.concat([s1, s2, s3], axis=1)
print(d)


