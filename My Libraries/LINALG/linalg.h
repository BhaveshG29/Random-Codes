#ifndef LINALG_H
#define LINALG_H

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Core matrix operations
int determinant(double **matrix, int n);
void matrix_multiply(double **A, int rowsA, int colsA, double **B, int rowsB, int colsB, double **result);
void find_eigenvalues(double **matrix, int n, double *eigenvalues, int max_iterations);
void find_eigenvectors(double **matrix, int n, double *eigenvalues, double **eigenvectors);

// Additional utility functions
void matrix_transpose(double **matrix, int rows, int cols, double **result);
void matrix_inverse(double **matrix, int n, double **result);
void matrix_add(double **A, double **B, int rows, int cols, double **result);
void matrix_subtract(double **A, double **B, int rows, int cols, double **result);
double matrix_trace(double **matrix, int n);

// Memory allocation helpers
double **allocate_matrix(int rows, int cols);
void free_matrix(double **matrix, int rows);
void print_matrix(double **matrix, int rows, int cols);

#endif

