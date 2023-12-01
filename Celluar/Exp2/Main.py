import matplotlib.pyplot as plt
import matplotlib.animation as animation
import SIM
from time import sleep

grid_size = 500

D0 = 0.7
D1_5 = 0
D2_5 = 0
D3_5 = .1
D4_5 = 0
D1 = 0.2
d = (D1,D4_5,D3_5,D2_5,D1_5,D0)

i = SIM.I(grid_size,d,1)

fig, ax = plt.subplots()


grid = i.grid
# create an image plot of the grid
im = ax.imshow(grid, cmap='gray')




def update(frame):
    # update the grid with random values
    i.frame()
    im.set_data(grid)
    sleep(0.01)
    return [im]

# create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()