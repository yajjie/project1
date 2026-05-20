import pandas as pd

data = [

    ["Amy", 23, 88],

    ["Bob", 25, 92],

    ["Cathy", 22, 79]

]

df = pd.DataFrame(data, columns=["name", "age", "score"])

print(df.head())
