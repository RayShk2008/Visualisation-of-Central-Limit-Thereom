import numpy as np
import matplotlib.pyplot as plt
n = int(input("n = "))
def sample_means_exp_sim(n, trials, scale=1.0): #scale = 1.0 sets the mean of the exponential distrubution to 1.
#numpy uses "scale"/mean rather than "rate"/lambda
    sample_means = []
    for i in range(trials):
        sample = np.random.exponential(scale=scale, size=n)
        sample_means.append(np.mean(sample))
    return np.array(sample_means)

plt.hist(sample_means_exp_sim(n, 10000), bins=30)
plt.title("Sample Means from an Exponential Distrubution")
plt.show()