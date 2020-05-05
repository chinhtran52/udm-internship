import open3d as o3d

pcd = o3d.io.read_point_cloud('./Mesh/results/8 frames/jean_ng1.ply')
mesh = o3d.io.read_triangle_mesh('./Mesh/results/8 frames/jean_ng1.ply')
o3d.visualization.draw_geometries([mesh])