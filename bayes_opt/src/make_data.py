import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')


def f(x):
    theta1 = np.pi * x
    theta2 = 2 * np.pi * x
    return np.sin(theta1) * np.cos(theta2)


def main():
    n = 100
    x = np.linspace(-1, 1, n)
    noise = np.random.normal(size=n)
    y = f(x) +  0.1 * noise
    data = np.vstack((x, y)).T
    np.savetxt(fname='../data/data.txt', X=data, header='x,y')

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
