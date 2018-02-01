#ifndef VORONOI_H_
#define VORONOI_H_

#include "gl_libs.h"

typedef CGAL::Exact_predicates_inexact_constructions_kernel  K;
typedef CGAL::Polyhedron_3<K>                     Polyhedron_3;
typedef K::Point_3                                Point_3;
typedef CGAL::Surface_mesh<Point_3>               Surface_mesh;

typedef Polyhedron_3::Vertex  Vertex;
typedef Polyhedron_3::Vertex_iterator  Vertex_iterator;
typedef Polyhedron_3::Halfedge_handle  Halfedge_handle;
typedef Polyhedron_3::Edge_iterator  Edge_iterator;
typedef Polyhedron_3::Facet_iterator  Facet_iterator;
typedef Polyhedron_3::Halfedge_around_facet_circulator HF_circulator;


namespace voronoi {
  int generate_voronoi(int num_pts, std::vector<glm::vec3> *g_vertex_buffer_data, std::vector<glm::vec3> *g_color_buffer_data);
  int generate_random_points(int num, std::vector<Point_3> *res);
  int calculate_centers(Polyhedron_3 poly, std::vector<Point_3> *res);
}

#endif  // VORONOI_H_
