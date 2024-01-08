import open3d as o3d
import laspy
import numpy as np

nums = [2672,2673,2674,2572,2573,2574]
paths = [f"NT{num}_4PPM_LAS_PHASE5" for num in nums]
print(paths)

las = laspy.read('NT2572_4PPM_LAS_PHASE5.laz')

x = las.X 
y = las.Y 
z = las.Z 

xyz = np.dstack([x,y,z])[0]

pcd = o3d.geometry.PointCloud()

pcd.points = o3d.utility.Vector3dVector(xyz[:,:3])


# Display the selected point cloud
o3d.visualization.draw_geometries([pcd])