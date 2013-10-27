# sample Makefile to compile and execute the 
# C files

run:	compile
	./gsl_vector
	./omp_demo

compile: gsl_vector omp_demo

gsl_vector:
	gcc -o gsl_vector gsl_vector.c -lgsl

omp_demo:
	gcc -o omp_demo omp_demo.c -lgomp

.PHONY: compile
