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

#Hexbin plot
df2=pd.DataFrame({
    'X': np.random.randn(1000),
    'y': np.random.randn(1000)+1

})

df2.plot(kind='hexbin',x='X',y='y',gridsize=30,cmap='viridis')
plt.title('Hexbin Plot of Random Data')
plt.show()