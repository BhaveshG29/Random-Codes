#include "linalg.h"

// Helper function to get absolute value
double abs_val(double x) {
    return x < 0 ? -x : x;
}

// Helper function for matrix copying
void copy_matrix(double **src, double **dest, int rows, int cols) {
    int i, j;
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            dest[i][j] = src[i][j];
        }
    }
}

// Memory allocation for matrix
double **allocate_matrix(int rows, int cols) {
    double **matrix;
    int i;
    
    matrix = (double **)malloc(rows * sizeof(double *));
    if(matrix == NULL) return NULL;
    
    for(i = 0; i < rows; i++) {
        matrix[i] = (double *)malloc(cols * sizeof(double));
        if(matrix[i] == NULL) {
            // Free previously allocated memory
            int j;
            for(j = 0; j < i; j++) {
                free(matrix[j]);
            }
            free(matrix);
            return NULL;
        }
    }
    return matrix;
}

// Free matrix memory
void free_matrix(double **matrix, int rows) {
    int i;
    for(i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

// Print matrix
void print_matrix(double **matrix, int rows, int cols) {
    int i, j;
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            printf("%.4f\t", matrix[i][j]);
        }
        printf("\n");
    }
}

// Calculate determinant using Gaussian elimination
int determinant(double **matrix, int n) {
    double **temp = allocate_matrix(n, n);
    double det = 1.0;
    int i, j, k;
    int sign = 1;
    
    // Copy matrix to avoid modifying original
    copy_matrix(matrix, temp, n, n);
    
    // Gaussian elimination with partial pivoting
    for(i = 0; i < n; i++) {
        // Find pivot
        int max_row = i;
        for(k = i + 1; k < n; k++) {
            if(abs_val(temp[k][i]) > abs_val(temp[max_row][i])) {
                max_row = k;
            }
        }
        
        // Swap rows if needed
        if(max_row != i) {
            double *temp_row = temp[i];
            temp[i] = temp[max_row];
            temp[max_row] = temp_row;
            sign = -sign;
        }
        
        // Check for singular matrix
        if(abs_val(temp[i][i]) < 1e-10) {
            free_matrix(temp, n);
            return 0;
        }
        
        // Eliminate column
        for(k = i + 1; k < n; k++) {
            double factor = temp[k][i] / temp[i][i];
            for(j = i; j < n; j++) {
                temp[k][j] -= factor * temp[i][j];
            }
        }
        
        det *= temp[i][i];
    }
    
    det *= sign;
    free_matrix(temp, n);
    return (int)det;
}

// Matrix multiplication
void matrix_multiply(double **A, int rowsA, int colsA, double **B, int rowsB, int colsB, double **result) {
    int i, j, k;
    
    if(colsA != rowsB) {
        printf("Error: Matrix dimensions incompatible for multiplication\n");
        return;
    }
    
    // Initialize result matrix to zero
    for(i = 0; i < rowsA; i++) {
        for(j = 0; j < colsB; j++) {
            result[i][j] = 0.0;
        }
    }
    
    // Perform multiplication
    for(i = 0; i < rowsA; i++) {
        for(j = 0; j < colsB; j++) {
            for(k = 0; k < colsA; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

// Find eigenvalues using QR iteration (simplified)
void find_eigenvalues(double **matrix, int n, double *eigenvalues, int max_iterations) {
    double **A = allocate_matrix(n, n);
    double **Q = allocate_matrix(n, n);
    double **R = allocate_matrix(n, n);
    int iter, i, j, k;
    
    copy_matrix(matrix, A, n, n);
    
    // QR iteration for eigenvalues
    for(iter = 0; iter < max_iterations; iter++) {
        // Simple QR decomposition using Gram-Schmidt
        // Initialize Q as identity
        for(i = 0; i < n; i++) {
            for(j = 0; j < n; j++) {
                Q[i][j] = (i == j) ? 1.0 : 0.0;
                R[i][j] = 0.0;
            }
        }
        
        // Gram-Schmidt process (simplified)
        for(j = 0; j < n; j++) {
            // Copy column j of A to Q
            for(i = 0; i < n; i++) {
                Q[i][j] = A[i][j];
            }
            
            // Orthogonalize against previous columns
            for(k = 0; k < j; k++) {
                double dot_product = 0.0;
                for(i = 0; i < n; i++) {
                    dot_product += Q[i][k] * A[i][j];
                }
                R[k][j] = dot_product;
                
                for(i = 0; i < n; i++) {
                    Q[i][j] -= dot_product * Q[i][k];
                }
            }
            
            // Normalize
            double norm = 0.0;
            for(i = 0; i < n; i++) {
                norm += Q[i][j] * Q[i][j];
            }
            norm = sqrt(norm);
            R[j][j] = norm;
            
            if(norm > 1e-10) {
                for(i = 0; i < n; i++) {
                    Q[i][j] /= norm;
                }
            }
        }
        
        // A = R * Q
        matrix_multiply(R, n, n, Q, n, n, A);
    }
    
    // Extract eigenvalues from diagonal
    for(i = 0; i < n; i++) {
        eigenvalues[i] = A[i][i];
    }
    
    free_matrix(A, n);
    free_matrix(Q, n);
    free_matrix(R, n);
}

// Find eigenvectors using power method
void find_eigenvectors(double **matrix, int n, double *eigenvalues, double **eigenvectors) {
    int i, j, k;
    double **A_shifted = allocate_matrix(n, n);
    double *v = (double *)malloc(n * sizeof(double));
    double *v_new = (double *)malloc(n * sizeof(double));
    
    for(i = 0; i < n; i++) {
        // Create A - λI for each eigenvalue
        for(j = 0; j < n; j++) {
            for(k = 0; k < n; k++) {
                A_shifted[j][k] = matrix[j][k];
                if(j == k) A_shifted[j][k] -= eigenvalues[i];
            }
        }
        
        // Initialize random vector
        for(j = 0; j < n; j++) {
            v[j] = 1.0;
        }
        
        // Inverse power method iterations
        for(int iter = 0; iter < 100; iter++) {
            // Solve (A - λI)v_new = v using simple Gaussian elimination
            // This is simplified - in practice would use LU decomposition
            double sum;
            for(j = 0; j < n; j++) {
                sum = 0.0;
                for(k = 0; k < n; k++) {
                    if(k != j && abs_val(A_shifted[j][j]) > 1e-10) {
                        sum += A_shifted[j][k] * v_new[k];
                    }
                }
                if(abs_val(A_shifted[j][j]) > 1e-10) {
                    v_new[j] = (v[j] - sum) / A_shifted[j][j];
                } else {
                    v_new[j] = v[j];
                }
            }
            
            // Normalize
            double norm = 0.0;
            for(j = 0; j < n; j++) {
                norm += v_new[j] * v_new[j];
            }
            norm = sqrt(norm);
            
            if(norm > 1e-10) {
                for(j = 0; j < n; j++) {
                    v_new[j] /= norm;
                    v[j] = v_new[j];
                }
            }
        }
        
        // Store eigenvector
        for(j = 0; j < n; j++) {
            eigenvectors[i][j] = v[j];
        }
    }
    
    free_matrix(A_shifted, n);
    free(v);
    free(v_new);
}

// Matrix transpose
void matrix_transpose(double **matrix, int rows, int cols, double **result) {
    int i, j;
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            result[j][i] = matrix[i][j];
        }
    }
}

// Matrix inverse using Gauss-Jordan elimination
void matrix_inverse(double **matrix, int n, double **result) {
    double **augmented = allocate_matrix(n, 2*n);
    int i, j, k;
    
    // Create augmented matrix [A|I]
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            augmented[i][j] = matrix[i][j];
            augmented[i][j + n] = (i == j) ? 1.0 : 0.0;
        }
    }
    
    // Gauss-Jordan elimination
    for(i = 0; i < n; i++) {
        // Find pivot
        int max_row = i;
        for(k = i + 1; k < n; k++) {
            if(abs_val(augmented[k][i]) > abs_val(augmented[max_row][i])) {
                max_row = k;
            }
        }
        
        // Swap rows
        if(max_row != i) {
            double *temp_row = augmented[i];
            augmented[i] = augmented[max_row];
            augmented[max_row] = temp_row;
        }
        
        // Check for singular matrix
        if(abs_val(augmented[i][i]) < 1e-10) {
            printf("Error: Matrix is singular\n");
            free_matrix(augmented, n);
            return;
        }
        
        // Scale pivot row
        double pivot = augmented[i][i];
        for(j = 0; j < 2*n; j++) {
            augmented[i][j] /= pivot;
        }
        
        // Eliminate column
        for(k = 0; k < n; k++) {
            if(k != i) {
                double factor = augmented[k][i];
                for(j = 0; j < 2*n; j++) {
                    augmented[k][j] -= factor * augmented[i][j];
                }
            }
        }
    }
    
    // Extract inverse matrix
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            result[i][j] = augmented[i][j + n];
        }
    }
    
    free_matrix(augmented, n);
}

// Matrix addition
void matrix_add(double **A, double **B, int rows, int cols, double **result) {
    int i, j;
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            result[i][j] = A[i][j] + B[i][j];
        }
    }
}

// Matrix subtraction
void matrix_subtract(double **A, double **B, int rows, int cols, double **result) {
    int i, j;
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            result[i][j] = A[i][j] - B[i][j];
        }
    }
}

// Matrix trace (sum of diagonal elements)
double matrix_trace(double **matrix, int n) {
    double trace = 0.0;
    int i;
    for(i = 0; i < n; i++) {
        trace += matrix[i][i];
    }
    return trace;
}

