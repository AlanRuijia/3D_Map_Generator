#! /usr/bin/env python
import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection 
from mpl_toolkits.mplot3d.art3d import Line3DCollection 
from scipy.spatial import SphericalVoronoi
from scipy.spatial import ConvexHull

is_farthest = True
num_points = 10

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

def get_vertex_centers(sv):
  new_points = np.array([])
  for region in sv.regions:
    size = len(region)
    new_point = np.array([0, 0, 0])
    for pindex in region:
      new_point = np.sum([new_point, sv.vertices[pindex]],axis=0)
    norm = np.linalg.norm(new_point)
    new_point /= norm
    if len(new_points) == 0:
      new_points = np.array([new_point])
    else:
      new_points = np.append(new_points, [new_point], axis=0)
  return new_points

def plot_convex_hull(CH, fig, num):
  ax = fig.add_subplot(num, projection='3d')
  # plot the unit sphere for reference (optional)
  u = np.linspace(0, 2 * np.pi, 100)
  v = np.linspace(0, np.pi, 100)
  x = np.outer(np.cos(u), np.sin(v))
  y = np.outer(np.sin(u), np.sin(v))
  z = np.outer(np.ones(np.size(u)), np.cos(v))
  ax.plot_surface(x, y, z, color='y', alpha=0.1)
  ax.scatter(CH.simplices[:, 0], CH.simplices[:, 1], CH.simplices[:, 2], c='r')


def plot_voronoi(sv, fig, num, title):
  ax = fig.add_subplot(num, projection='3d')
  # plot the unit sphere for reference (optional)
  u = np.linspace(0, 2 * np.pi, 100)
  v = np.linspace(0, np.pi, 100)
  x = np.outer(np.cos(u), np.sin(v))
  y = np.outer(np.sin(u), np.sin(v))
  z = np.outer(np.ones(np.size(u)), np.cos(v))
  ax.plot_surface(x, y, z, color='#cc9900', alpha=0.3)
  # plot generator points
  # print("sv.points", sv.points)
  if is_farthest:
    ax.scatter(-(sv.points[:, 0]), -(sv.points[:, 1]), -(sv.points[:, 2]), c='k', s=30)
  else:
    ax.scatter((sv.points[:, 0]), (sv.points[:, 1]), (sv.points[:, 2]), c='k', s=30)
  
  # # plot Voronoi vertices
  ax.scatter(sv.vertices[:, 0], sv.vertices[:, 1], sv.vertices[:, 2], c='b', s=20)
  # indicate Voronoi regions (as Euclidean polygons)
  for region in sv.regions:
    random_color = colors.rgb2hex(np.random.rand(3))
    vertices = np.append(sv.vertices[region], [sv.vertices[region[0]]], axis=0)
    for ind in range(len(vertices)-1):
      point1 = vertices[ind]
      point2 = vertices[ind+1]
      point_set_x = np.linspace(point1[0], point2[0])
      point_set_y = np.linspace(point1[1], point2[1])
      point_set_z = np.linspace(point1[2], point2[2])
      point_set = np.stack((point_set_x, point_set_y, point_set_z), axis=-1)
      norms = np.stack([np.linalg.norm(point_set, axis=1)]*3, axis=-1)
      point_set /= norms
      ax.plot(point_set[:, 0], point_set[:, 1], point_set[:, 2], alpha=1.0)
      # polygon.set_color(random_color)
      # ax.add_collection3d(polygon)
  ax.set_title(title)
  return ax

def compare_curr(curr, prev):
  for ind in range(len(prev)):
    if not np.allclose(curr[ind], prev[ind]):
      return 0
  return 1

if __name__ == "__main__":
  phi = np.linspace(0, np.pi, 20)
  theta = np.linspace(0, 2 * np.pi, 40)
  x = np.outer(np.sin(theta), np.cos(phi))
  y = np.outer(np.sin(theta), np.sin(phi))
  z = np.outer(np.cos(theta), np.ones_like(phi))
  for zz in range(1):
    print(zz)
    xi, yi, zi = sample_spherical(num_points)

    p = np.stack((xi, yi, zi), axis=-1)
    print(p)
    if is_farthest:
      xi = -xi
      yi = -yi
      zi = -zi
    fig = plt.figure()
    points = np.array([[xi[0], yi[0], zi[0]]])
    for i in range(1,len(xi)):
      points = np.append(points, [[xi[i], yi[i], zi[i]]], axis=0)

    center = np.array([0, 0, 0])
    radius = 1
    sv = SphericalVoronoi(points, radius, center)
    curr_array = []
    curr = []
    sv.sort_vertices_of_regions()
    for region in sv.regions:
      for v in sv.vertices[region]:
        curr.append(v)
    curr_array.append(curr)
    plot_voronoi(sv, fig, 211, ("Nearest neighbor " if not is_farthest else "Farthest Point ") + "Voronoi Diagram for\n" + str(num_points) + " random points")

    stop_flag = 0
    for i in range(0,300):
      if stop_flag == 1 :
        print("same or recursive", i)
        break
      points = get_vertex_centers(sv)
      sv = SphericalVoronoi(points, radius, center)
      sv.sort_vertices_of_regions()
      curr = []
      for region in sv.regions:
        for v in sv.vertices[region]:
          curr.append(v)
      for prev in curr_array:
        if compare_curr(curr, prev):
          stop_flag = 1
          break
      curr_array.append(curr)


    sv.sort_vertices_of_regions()
    ax = plot_voronoi(sv, fig, 212, ("Nearest neighbor " if not is_farthest else "Farthest Point ") + "Voronoi Diagram for\n" + str(num_points) + " points")
    plt.show()