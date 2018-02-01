#ifndef INIT_SHADER_H_
#define INIT_SHADER_H_

#include "gl_libs.h"

namespace angel {

// Helper function to read a shader source file and return its content
char *ReadShaderSource(const char *shader_file);

// Helper function to load vertex and fragment shader files
GLuint InitShader(const char* vertex_shader_file, const char* fragment_shader_file);

} // namespace angle

#endif  // INIT_SHADER_H_
