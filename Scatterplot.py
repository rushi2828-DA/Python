#types of plot in pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data={
    'Month': ['Jan','Feb','Mar','Apr','May'],
    'Sales': [200,250,300,280,320],
    'Profit': [50,70,90,85,95]
}

df=pd.DataFrame(data)

#ScatterPlot
df.plot(kind='scatter',x='Sales',y='Profit',color='green')
plt.title("Sales vs Profit - Scatter Plot")
plt.show()