import open3d as o3d
import laspy
import numpy as np
from os import listdir

paths = listdir("Edinburgh")

laslist = [laspy.read(f'Edinburgh/{path}') for path in paths]

x = laslist[0].X
y = laslist[0].Y
z = laslist[0].Z


for las in laslist[1:]:
    print(las.header.x_offset)
    print(las.header.y_offset)
    print(las.header.z_offset)
    print(las.header.min[0],end="\n\n")
    """x = np.append(x,las.X + (1_000_000 * ((las.header.min[0] - laslist[0].header.min[0])/1_000)))
    y = np.append(y,las.Y + (1_000_000 * ((las.header.min[1] - laslist[0].header.min[1])/1_000)))"""#this works too, offset is just some kinda global value of location
    x = np.append(x,las.X + (1_000_000 * (las.header.x_offset - laslist[0].header.x_offset)/1_000))
    y = np.append(y,las.Y + (1_000_000 * (las.header.y_offset - laslist[0].header.y_offset)/1_000))
    z = np.append(z,las.Z + (1_000_000 * (las.header.z_offset - laslist[0].header.z_offset)/1_000))



xyz = np.dstack([x,y,z])[0]

pcd = o3d.geometry.PointCloud()

pcd.points = o3d.utility.Vector3dVector(xyz[:,:3])


# Display the selected point cloud
o3d.visualization.draw_geometries([pcd])