import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0,1.0,1000)

plt.subplot(1,2,1) # 1 row, 2 columns, 1st plot    . Bell shaped curve
x = np.random.normal(0.0,1.0,10000)
plt.hist(x)

plt.subplot(1,2,2)
x = np.random.uniform(-3.0,3.0,10000) # 1 row, 2 columns, 2nd plot. Expect  astraight line
plt.hist(x)


plt.show()
