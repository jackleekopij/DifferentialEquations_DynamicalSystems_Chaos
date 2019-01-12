

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def main():
    numframes = 10000
    X = [0]
    Y = [0]
    for i in range(1000000):
        simulated_prob = np.random.uniform(0, 100)
        if simulated_prob < 1.0:
            x = 0
            y = 0.16 * Y[i - 1]
        elif simulated_prob < 86:
            x = 0.85 * X[i - 1] + 0.04 * Y[i - 1]
            y = -0.04 * X[i - 1] + 0.85 * Y[i - 1] + 1.60
        elif simulated_prob < 93:
            x = 0.20 * X[i - 1] - 0.26 * Y[i - 1]
            y = 0.23 * X[i - 1] + 0.22 * Y[i - 1] + 1.60
        else:
            x = -0.15 * X[i - 1] + 0.28 * Y[i - 1]
            y = 0.26 * X[i - 1] + 0.24 * Y[i - 1] + 0.44
        X.append(x)
        Y.append(y)

    #numpoints = 10
    #color_data = np.random.random((numframes, numpoints))
    #x, y, c = np.random.random((3, numpoints))

    tupled_data = [np.array(a) for a in zip(X,Y)]
    fig = plt.figure(figsize = [8,15])
    plt.axis([-3, 3, -1, 13])

    scat = plt.scatter(X[0], Y[0],marker = '.')


    ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes),
                                  fargs=(X,Y, scat), interval=1)
    plt.show()

def update_plot(i, x,y, scat):
    print(i)
    i = i ** (3/2)
    #data = np.hstack((x[:i, np.newaxis], y[:i, np.newaxis]))
    scat.set_offsets(np.c_[x[:i], y[:i]])
    return scat,

main()