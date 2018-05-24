import numpy as np
from matplotlib import pyplot as plt

print "Hello world"

a = np.array([1, 2, 3])
print a

plt.plot(range(len(a)), a)
plt.show()


