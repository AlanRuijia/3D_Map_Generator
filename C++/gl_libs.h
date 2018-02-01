#ifndef GL_LIBS_H_
#define GL_LIBS_H_

#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/Polyhedron_3.h>
#include <CGAL/Surface_mesh.h>
#include <CGAL/convex_hull_3.h>

#include <GL/glew.h>
#include <OpenGL/glu.h>
#ifdef __APPLE__
# define __gl_h_
# define GL_DO_NOT_WARN_IF_MULTI_GL_VERSION_HEADERS_INCLUDED
#endif
#include <OpenGL/gl3.h>
#include <GLUT/glut.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/ext.hpp>

#endif  // GL_LIBS_H_
