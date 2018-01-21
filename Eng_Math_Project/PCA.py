import matplotlib.pyplot as plt
import numpy as np


mean1 = np.transpose([10, 10])
mean2 = np.transpose([22, 10])

cov = [[4, 4], [4, 9]]
class_1 = np.random.multivariate_normal(mean1, cov, 1000).T
class_2 = np.random.multivariate_normal(mean2, cov, 1000).T

plt.plot(class_1[0, :], class_1[1, :], '+')
plt.plot(class_2[0, :], class_2[1, :], '+')
plt.axis('equal')
plt.show()

