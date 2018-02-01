CC=g++
PFLAGS=-Wall -ansi -pedantic -O2 -I/usr/local/include -I/usr/local/lib 
CFLAGS=-lCGAL -lgmp -lglfw.3 -lGLEW -framework OpenGL -framework GLUT 
DEPS=init_shader.h gl_libs.h voronoi.h

%.o: %.cpp $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

all: main.o init_shader.o voronoi.o
	$(CC) $(PFLAGS) main.o init_shader.o voronoi.o -o main $(CFLAGS)

clean: 
	rm *.o