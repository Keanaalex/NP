# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

inputCsv = np.genfromtxt('pntcloud_frame_0_time_2021-05-11_10-55-17.837_PDT.csv',delimiter = ',')

selectedData = inputCsv[1:10000,2:5]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for i in range(len(selectedData)):
        ax.scatter(selectedData[i][0],selectedData[i][1],selectedData[i][2])
        plt.show()