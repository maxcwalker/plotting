#include<stdio.h>
#include<stdlib.h>
#include<math.h>


///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

void print_matrix(int n, double a[3][3]){
    int i,j;

    for(i=0; i<n; i++){
        printf("|\t");
        for (j=0; j<n; j++){
            printf("%.1f\t",a[i][j]);
            }
        printf("|\n");
        }
}

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

double transpose(double a[3][3]){
    int i,j;

    double **a0;

    a0 = (double **)malloc(sizeof(double *)*3);
    a0[0] = (double *)malloc(3*sizeof(double));
    a0[1] = (double *)malloc(3*sizeof(double));
    a0[2] = (double *)malloc(3*sizeof(double));


    for (i=0; i<3; i++){
        for (j=0; j<3; j++){
            a0[j][i] = a[i][j];
        }
    }
    for (i=0; i<3; i++){
        for (j=0; j<3; j++){
            a[i][j] = a0[i][j];
        }
    }
    return a[3][3];
}

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

double det2(double **a){
    return a[0][0]*a[1][1] - a[0][1]*a[1][0];
}

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

double cofactor(double a[3][3],int i,int j){
    double c;
    double **aij;
    aij = (double **)malloc(sizeof(double *)*2);
    aij[0] = (double *)malloc(2*sizeof(double));
    aij[1] = (double *)malloc(2*sizeof(double));

    int l,k;
    k=0;
    for(int x=0;x<3;x++)
    {
        l = 0;
        if(x != i){
            for(int y=0; y<3; y++){
                if(y!=j){
                    aij[k][l] = a[x][y];
                    l++;
                }   
            }
        k++;
        }
    }

    c = pow(-1,(i+j))*det2(aij); 

    return c;
}

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

double det3(double a[3][3]){
    int i=2,k;

    double det = 0;
    for (k=0; k<3; k++){
        det += a[k][i]*cofactor(a,k,i);
    }
    return det;
}

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

double inverse(double a[3][3]){
    // double **inv_a;
    // inv_a = (double **)malloc(sizeof(double *)*3);
    // inv_a[0] = (double *)malloc(3*sizeof(double));
    // inv_a[1] = (double *)malloc(3*sizeof(double));
    // inv_a[2] = (double *)malloc(3*sizeof(double));
    // double **a_trans;
    double inv_a[3][3];

    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            inv_a[i][j] = cofactor(a,j,i) / det3(a);
        }
    }


    return inv_a[3][3];
}

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

void multiply(double a[3][3], double b[3][3]){
    int i,j,k;

    double c[3][3] = {{0.0, 0.0, 0.0}, {0.0, 0.0, 0.0}, {0.0, 0.0, 0.0}};

    for(k=0; k<3; k++){
        for(i=0; i<3; i++){
            for(j=0; j<3; j++){
                c[k][i] += a[k][j]*b[j][i];
            }
        }
    }

    print_matrix(3, c);

}

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

int main(){

    double a[3][3] = {{1.0, 0.0, 1.0}, {0.0, 1.0, 1.0}, {0.0, 0.0, 1.0}};
    cofactor(a,0,0);

    printf("\nOriginal matrix:\n");
    print_matrix(3, a);

    printf("Determinant of the matrix:\n");
    printf("%f\n", det3(a));

    printf("\nTranspose of the matrix:\n");
    transpose(a);
    print_matrix(3, a);

    printf("Inverse of the matrix:\n");
    transpose(a);  // transpose back to obtain original matrix
    
    int i,j;
    
    double ainv[3][3];

    for(i=0; i<3; i++){ 
        for(j=0; j<3; j++){
            ainv[i][j] = a[i][j]; // copy of a to invert inverse(ainv);
        }
    }
    print_matrix(3, ainv);
    printf("Check that the product gives unit matrix.\n");
    multiply(a, ainv);
    return 0;
}