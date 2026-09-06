import matplotlib.pyplot as plt
import numpy as np

n = int(input("n = "))
def sample_means_sim(dice, trials): #parameters are the number of dice and the number of trials
    sample_means = []
    for i in range(trials):
        rolls = np.random.randint(1, 7, size=dice)
        sample_means.append(np.mean(rolls))
    return np.array(sample_means)

mean_of_n = sample_means_sim(n, 10000)

plt.hist(mean_of_n, bins=60)
plt.title("Distrubution of Sample Means for 10 dice")
plt.xlabel("Sample Mean")
plt.ylabel("Frequencey")
plt.show()