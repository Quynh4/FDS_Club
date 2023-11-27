import numpy as np
import pandas as pd
from sklearn import impute
data = pd.read_csv('data.csv', header=None)
X = data.values
imp = impute.SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(X)
print(imp.transform(X))