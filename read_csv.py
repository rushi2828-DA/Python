import pandas as pd

df=pd.read_csv('data.csv')
#print(df.to_string())   #df.to string full entire data
#use to_string() to print the entire DataFrame

#print(df)  #df-only first five rows

#print(df.head)  #df.head-only first 5 row show

print(df.tail)  #df.tail -only last 5 rowwill show


#use to_string() to print the entire DataFrame.


print(pd.__version__)