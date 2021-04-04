from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(5, 8))

grid_size = 32

p = np.zeros((grid_size, grid_size))
p[16][16] = 1
p[16][17] = 1

im = plt.imshow(p, animated=True)


def update(i):
    y_order = list(range(p.shape[0]))
    x_order = list(range(p.shape[1]))
    np.random.shuffle(y_order)
    np.random.shuffle(x_order)
    for y in y_order:
        for x in x_order:
            if p[x][y] != 0:
                if p[x-1][y] != p[x][y]:
                    if p[x+1][y] == 0:
                        p[x+1][y] = p[x][y]
                        p[x][y] = 0
                if p[x+1][y] != p[x][y]:
                    if p[x-1][y] == 0:
                        p[x-1][y] = p[x][y]
                        p[x][y] = 0
                if p[x][y-1] != p[x][y]:
                    if p[x][y+1] == 0:
                        p[x][y+1] = p[x][y]
                        p[x][y] = 0
                if p[x][y+1] != p[x][y]:
                    if p[x][y-1] == 0:
                        p[x][y-1] = p[x][y]
                        p[x][y] = 0

    im.set_array(p)


anim = FuncAnimation(fig, update, frames=np.arange(0, 20), interval=1000)
# anim.save('colour_rotation.gif', dpi=80, writer='imagemagick')
# plt.close()
plt.show()
