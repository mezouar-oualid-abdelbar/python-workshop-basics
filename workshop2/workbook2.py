import pandas as pd

fruits = {'apple': 12.5 ,'banana' :20.0 ,'tomato':5.5 , 'water melon' : 44.7 ,'pinaple':455.5}

pdseries =pd.Series(fruits)

print(pdseries)

print(pdseries.iloc[2])

ps= pdseries * 1.1

print(ps)

print("avreage" ,ps.mean())
