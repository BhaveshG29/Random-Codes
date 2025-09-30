Overview:
This C library provides basic linear algebra operations. Include "linalg.h" in your C source to access the following functions.

1. determinant
   Use: Compute the determinant of an n×n matrix.
   Prototype: int determinant(double **matrix, int n);
   How to call:
     int det = determinant(matrix, n);

2. matrix_multiply
   Use: Multiply two matrices A (rowsA×colsA) and B (rowsB×colsB).
   Prototype: void matrix_multiply(double **A, int rowsA, int colsA,
                                 double **B, int rowsB, int colsB,
                                 double **result);
   How to call:
     matrix_multiply(A, rowsA, colsA, B, rowsB, colsB, result);

3. find_eigenvalues
   Use: Compute all eigenvalues of an n×n matrix using QR iteration.
   Prototype: void find_eigenvalues(double **matrix, int n,
                                    double *eigenvalues,
                                    int max_iterations);
   How to call:
     double eig[n];
     find_eigenvalues(A, n, eig, 100);

4. find_eigenvectors
   Use: Compute eigenvectors corresponding to given eigenvalues using the inverse power method.
   Prototype: void find_eigenvectors(double **matrix, int n,
                                      double *eigenvalues,
                                      double **eigenvectors);
   How to call:
     double **eigvecs = allocate_matrix(n, n);
     find_eigenvectors(A, n, eig, eigvecs);


5. matrix_transpose
   Use: Transpose a rows×cols matrix.
   Prototype: void matrix_transpose(double **matrix, int rows,
                                     int cols, double **result);
   How to call:
     matrix_transpose(A, rows, cols, transposed);

6. matrix_inverse
   Use: Invert an n×n matrix using Gauss-Jordan elimination.
   Prototype: void matrix_inverse(double **matrix, int n,
                                   double **result);
   How to call:
     matrix_inverse(A, n, inverse);

7. matrix_add
   Use: Element-wise addition of two matrices.
   Prototype: void matrix_add(double **A, double **B,
                               int rows, int cols,
                               double **result);
   How to call:
     matrix_add(A, B, rows, cols, sum);

8. matrix_subtract
   Use: Element-wise subtraction of two matrices.
   Prototype: void matrix_subtract(double **A, double **B,
                                    int rows, int cols,
                                    double **result);
   How to call:
     matrix_subtract(A, B, rows, cols, diff);

9. matrix_trace
   Use: Compute the trace (sum of diagonal) of an n×n matrix.
   Prototype: double matrix_trace(double **matrix, int n);
   How to call:
     double tr = matrix_trace(A, n);

Memory and I/O Helpers:

10. allocate_matrix
    Use: Allocate memory for a matrix of given dimensions.
    Prototype: double **allocate_matrix(int rows, int cols);
    How to call:
      double **M = allocate_matrix(rows, cols);

11. free_matrix
    Use: Free memory allocated by allocate_matrix.
    Prototype: void free_matrix(double **matrix, int rows);
    How to call:
      free_matrix(M, rows);

12. print_matrix
    Use: Print a matrix to stdout with formatting.
    Prototype: void print_matrix(double **matrix, int rows, int cols);
    How to call:
      print_matrix(A, rows, cols);

Compilation:
  gcc -c linalg.c -o linalg.o -lm
  ar rcs liblinalg.a linalg.o
  gcc main.c -L. -llinalg -o app

Include:
  #include "linalg.h"


