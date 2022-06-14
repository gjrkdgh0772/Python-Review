import numpy as np

arr =np.array([1, 2, 3])
print(arr)
print(arr,type(arr))    # array = 배열
num = int("1")


import pandas as pd
# data=None,
# index: Axes | None = None,
# columns: Axes | None = None,
# dtype: Dtype | None = None,
# copy: bool | None = None,
df = pd.DataFrame(data = [[1,'kim',111],[2,'lee',222]],
                  columns = ['seq','id','pw']
                  )

print(df.info())

import seaborn as sns
sns.heatmap

from sklearn.model_selection import cross_val_score
cross_val_score(model,)