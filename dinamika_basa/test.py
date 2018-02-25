# from matplotlib import pyplot as plt
import numpy as np
# import matplotlib

# x = np.arange(0.0, 50.0, 2.0)
# y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
# s = np.random.rand(*x.shape) * 800 + 500

# plt.plot(x, y, "ro", alpha=0.5, marker=r'$\perp$', markersize=22)
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.show()

for i in np.arange(100):
	if np.random.randint(2, size=1)==True:
		print(1)
	else:
		print(0)