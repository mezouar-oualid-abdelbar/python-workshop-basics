import pandas as pd

products = {
    'Product': ['A', 'B', 'C', 'C' ,'A'],
    'Region': ['North', 'South', 'East', 'West','South'],
    'Amount': [50000, 55000, 70000, 65000 , 40000]
}

df=pd.DataFrame(products)

print(df)

print(df.groupby('Product').sum('Amount'))

print(df.groupby('Region').mean('Amount'))

print(df.groupby('Product')['Amount'].agg(['mean','max']))
