import matplotlib.pyplot as plt
from random import normalvariate

alpha = [0.98, 0.0,0.8]
ts_length = 200

for j in alpha:
	x_values = []
	current_x = 0
	for i in range(ts_length+1):
		x_values.append(current_x)

		current_x = j * current_x + normalvariate(0,1)
	plt.plot(x_values,label = "alpha =" + str(alpha))

plt.legend()
plt.show()


    


    