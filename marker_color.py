import matplotlib.pyplot as plt
import numpy as np

ypoints=([3,8,1,10])
#plt.plot(ypoints, marker='o', ms=20, mec='r') #ms=marker size  mec=marker external color
#plt.plot(ypoints, marker='o', ms=20, mfc='r') #ms=marker size  mfc=marker fill color

#plt.plot(ypoints, marker='o', ms=20, mec='r')
#plt.plot(ypoints, marker='o', ms=20, mfc='r')

#plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')  
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')  #we can use initial/color code/name
plt.show()