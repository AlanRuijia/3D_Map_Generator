#include "voronoi.h"
#include <cmath>
using namespace std;

int voronoi::generate_voronoi(int num_pts, std::vector<glm::vec3> *g_vertex_buffer_data, std::vector<glm::vec3> *g_color_buffer_data) {
  vector<Point_3> points;
  srand (time(NULL));
  
  voronoi::generate_random_points(num_pts, &points);
  // define polyhedron to hold convex hull
  Polyhedron_3 poly;
  
  for (int i = 0; i < 1; i++) {
    poly.clear();
    CGAL::convex_hull_3(points.begin(), points.end(), poly);
    // voronoi::calculate_pbs(poly, &points);
    voronoi::calculate_centers(poly, &points);
  }
  // compute convex hull of non-collinear points
  

  // std::cout << "The convex hull contains " << poly.size_of_vertices() << " vertices" << std::endl;
  // Surface_mesh sm;
  
  // CGAL::convex_hull_3(points.begin(), points.end(), sm);
  // std::cout << "The convex hull contains " << poly.size_of_facets() << " vertices" << std::endl;
  Facet_iterator f;
  for (f = poly.facets_begin(); f != poly.facets_end(); f++) {
    HF_circulator h = f->facet_begin();
    glm::vec3 temp_color(float(rand())/ RAND_MAX, float(rand())/ RAND_MAX, float(rand())/ RAND_MAX);
    do { 
      const Point_3& p  = h->vertex()->point(); 
      // ::glVertex3d(p.x(),p.y(),p.z()); 
      glm::vec3 temp_vertex(p.x(), p.y(), p.z());
      g_vertex_buffer_data -> push_back(temp_vertex);
      g_color_buffer_data -> push_back(temp_color);
      // cout << "point x: " << temp.x << " y: " << temp.y << " z: " << temp.z << endl;
    } 
    while(++h != f->facet_begin()); 
  }
  return 0;
}

int voronoi::generate_random_points(int num, vector<Point_3> *res){
  float theta, phi, x,y,z;
  if (res == NULL) {
    cout << "generate points error: res is null";
    return -1;
  }
  for (int i=0; i < num; i++) {
    theta = (float(rand()) / RAND_MAX) * 2.0 * M_PI;
    phi = (float(rand()) / RAND_MAX) * (M_PI) - 0.5 * M_PI;
    x = cos(theta) * cos(phi);
    y = sin(phi);
    z = sin(theta) * cos(phi);
    Point_3 tmp(x, y, z);
    res -> push_back(tmp);
  }
  return 0;
}

int voronoi::calculate_centers(Polyhedron_3 poly, vector<Point_3> *res) {
  res -> clear();
  Facet_iterator f;
  for (f = poly.facets_begin(); f != poly.facets_end(); f++) {
    HF_circulator h = f->facet_begin();
    glm::vec3 centroid(0.0f);
    do {
      const Point_3& p  = h->vertex()->point();
      centroid.x += p.x();
      centroid.y += p.y();
      centroid.z += p.z();
    } 
    while(++h != f->facet_begin()); 
    centroid = glm::normalize(centroid);
    Point_3 p_c(centroid.x, centroid.y, centroid.z);
    res -> push_back(p_c);
  }
  return 0;
}
