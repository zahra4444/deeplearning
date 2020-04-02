import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import  seaborn as sns
sns.set()
data=pd.read_csv('real_estate_price_size.csv')
data.head()
data.describe()
x1=data['size']
y= data['price']
plt.scatter(x1,y)
plt.xlabel('size')
plt.ylabel('price')
plt.show()
