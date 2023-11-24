import matplotlib.pyplot as plt
import matplotlib.animation as animation
import SIM as SIM

grid_size = (1500,1500)
p = (0.03,0.97)

Game = SIM.Game(grid_size,p)

fig, ax = plt.subplots()


grid = Game.grid
# create an image plot of the grid
im = ax.imshow(grid, cmap='gray')




def update(frame):
    # update the grid with random values
    Game.frame()
    im.set_data(grid)
    return [im]

# create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()