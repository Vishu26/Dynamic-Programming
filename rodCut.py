from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_mldata


plt.ion()
mnist = fetch_mldata('MNIST original')
X = mnist.data.astype('float64')
id = np.random.permutation(70000)
X = X[id]
y = mnist.target
y = y[id]
x = X.data
X = X.reshape(-1, 28, 28)

# Fixing random state for reproducibility
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].

xs1 = np.array([np.arange(0, 28) for i in range(28)])
ys1 =np.zeros((28, 28))

z = [np.ones(28)*i for i in range(28)]

for k in range(10):
    print(k)

    data = np.random.randint(500)

    for i in range(28):
        for j in range(28):
            ax.scatter(j, 0, i, c=(X[data][i][j]/255, 0 ,0), marker='o')

    for i in range(23):
        for j in range(23):
            ax.scatter(j+2, 5, i+2, c=(np.random.uniform(0, 1), 0, 0), marker='o')

    for i in range(16):
        for j in range(16):
            ax.scatter(j+5, 10, i+5, c=(np.random.uniform(0, 1), 0, 0), marker='o')

    for i in range(32):
        ax.scatter(14, 15, i-16, c = (np.random.uniform(0, 1), 0, 0), marker='o')
    for i in range(10):
        if y[data] == i:
            ax.scatter(14, 20, i-5, c=(0.95, 0, 0), marker='o')
        else:
            ax.scatter(14, 20, i - 5, c=(np.random.uniform(0, 1)/3, 0, 0), marker='o')
    plt.pause(0.005)

while True:
    plt.pause(0.005)







#for i in range(10)

'''ax.scatter(xs1, ys1, z, marker='o', cmap='gray')
xs2 = np.array([np.arange(0, 23) for i in range(23)]) + 2
ys2 =np.ones((23, 23))*5

z2 = np.array([np.ones(23)*i for i in range(23)]) + 2

ax.scatter(xs2, ys2, z2, c='k', marker='o', cmap='gray')






xs3 = np.array([np.arange(0, 16) for i in range(16)]) + 5
ys3 =np.ones((16, 16))*10

z3 = np.array([np.ones(16)*i for i in range(16)]) + 5
ax.scatter(xs3, ys3, z3, c='k', marker='o', cmap='gray')'''



'''for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()'''
