import pandas as pd

data = {
    'calories':[420,380,390],
    'duration':[50,40,45]
}

#load data as dataframe objects
df=pd.DataFrame(data,index=['Day1','Day2','Day3'])

print(df.loc['Day2'])