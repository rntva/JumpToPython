import numpy as np
import matplotlib.pyplot as plt

v1 = np.zeros(10, dtype=np.float32)
print(v1)

v2 = np.arange(10, dtype=np.uint64)
print(v2)

v2 *= 3
print(v2)

print(v2.mean())

num_points = 1000
vectors_set = []

for i in range(num_points) :
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.033)
    vectors_set.append([x1, y1])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

print(x_data, y_data)

plt.plot(x_data, y_data, 'ro')
plt.show()