import pandas as pd
import matplotlib.pyplot as plt

iris_df = pd.read_csv('./iris.csv')

print(iris_df.head(3))

mask = iris_df['species'] == 'virginica'

print(iris_df[mask].head(5))

print('min sepal length:' ,iris_df['sepal_width'].min() , 'max sepal length:' ,iris_df['sepal_width'].max() )

print('heighest average sepal length =' ,iris_df.groupby('species')['sepal_length'].mean().max() )

#4

fig, sc = plt.subplots(figsize=(7, 7))
sc.scatter(iris_df['petal_length'], iris_df['petal_width'])

sc.legend()
plt.show()

#5

iris_bar = iris_df.groupby('species')['sepal_length'].mean()

print(iris_bar)

fig, bar = plt.subplots(figsize=(5, 2.7), layout='constrained')

bar.bar(iris_bar.index, iris_bar.values)
bar.set_title('line')
bar.legend()
plt.show()