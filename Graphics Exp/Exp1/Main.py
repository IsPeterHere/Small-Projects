import matplotlib.pyplot as plt
import matplotlib.animation as animation
import SIM

grid_size = 400

D0 = 0.6
D1_5 = 0.1
D2_5 = 0
D3_5 = 0
D4_5 = 0.1
D1 = 0.2
d = (D1,D4_5,D3_5,D2_5,D1_5,D0)

i = SIM.I(grid_size,d,0.03,0.79)

fig, ax = plt.subplots()


grid = i.grid
# create an image plot of the grid
im = ax.imshow(grid, cmap='gray')




def update(frame):
    # update the grid with random values
    i.frame()
    im.set_data(grid)
    return [im]

# create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()