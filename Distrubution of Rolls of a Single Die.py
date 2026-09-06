import matplotlib.pyplot as plt #used for data visualisation
import numpy as np

roll = np.random.randint(1, 7, size=10000)
    
plt.hist(roll, bins=6) #"bins=6" how many bars the histogram is divided into
plt.title("Distrubution of rolls of a Single Die")
plt.xlabel("Value")
plt.ylabel("Frequencey")
plt.show()
n = int(input("n = "))