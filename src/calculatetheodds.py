import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1993)

all_walks = []
for i in range(10):
    random_walk = [0]

    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

        if np.random.rand() <= 0.001 :
            step = 0

    all_walks.append(random_walk)

# Convert all_walks to Numpy array
numpy_allwalks = np.array(all_walks)
plt.plot(numpy_allwalks)
plt.show()
plt.clf()
numpy_allwalks_transpose = np.transpose(numpy_allwalks)
plt.plot(numpy_allwalks_transpose)
plt.show()