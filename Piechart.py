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

#PiePlot
df.set_index('Month')['Sales'].plot(kind='pie',autopct='%1.1f%%')
plt.title('Sales Distribution - Pie Chart')
plt.ylabel('') # Hide Y Axis label
plt.show()