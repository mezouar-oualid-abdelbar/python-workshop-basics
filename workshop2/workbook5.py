import pandas as pd
import matplotlib.pyplot as plt

quarters = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Revenue": [12000, 15000, 13500, 18000]
}

df =pd.DataFrame(quarters)


fig, line = plt.subplots()
line.plot(df['Quarter'] ,df['Revenue'])
line.set_title("line")
line.set_xlabel('Quarters')
line.set_ylabel('Revenues')
line.legend()
plt.show()


fig, bar = plt.subplots(figsize=(5, 2.7), layout='constrained')

bar.bar(df['Quarter'], df['Revenue'])
bar.set_title('line')
bar.legend()
plt.show()

 

students = {
    'Name': ['Walid', 'Saber', 'Katib', 'Mohsen', 'Bashir'],
    'Score': [90, 30, 85, 70, 90]
}

df2 = pd.DataFrame(students)

fig, his = plt.subplots(figsize=(5, 4), layout='constrained')

n, bins, patches = his.hist(
    df2['Score'],
    bins=10   
)

his.set_xlabel('Scores')
his.set_ylabel('Students')
his.set_title('Histogram')
his.grid(True, axis='y')
his.legend()
plt.show() 
 