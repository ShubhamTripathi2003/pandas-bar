#Made By Shubham Tripathi ---- Github


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_used_cars = pd.read_csv("amazon.csv")
print(df_used_cars)
sns.set()
plt.figure(figsize=(9,6))
plt.bar(x=df_used_cars['Supplier_Name'],height=df_used_cars['Price(in $)'])
plt.title('Sales Report')
plt.xticks(rotation=45)
plt.show()