import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
mylables=['Apples','Bananas','Cherries','Dates']

plt.pie(y,labels=mylables, startangle=90)

plt.show()