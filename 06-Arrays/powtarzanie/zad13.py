import matplotlib.pyplot as plt
import numpy as np

x = np.array([25,19,32,7])
y = np.array(["by car", "by public transport", "by bike", "on foot"])

plt.bar(y,x)
plt.show()