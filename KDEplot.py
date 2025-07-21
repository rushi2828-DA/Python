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


#KDE plot(kernel density estimate)
df['Sales'].plot(kind='kde',color='brown')
plt.title('Sales Density - KDE plot')
plt.show()