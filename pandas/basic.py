# Example from http://pandas.pydata.org/pandas-docs/stable/visualization.html#visualization

import matplotlib.pyplot as plt
from numpy.random import randn
from pandas import Series, date_range, DataFrame

ts = Series(randn(1000), index=date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()

df = DataFrame(randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.plot()
plt.show()
