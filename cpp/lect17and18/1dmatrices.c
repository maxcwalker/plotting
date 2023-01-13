#include<stdio.h>
#include<stdlib.h>
#define N 2

void multiply(double *a, double *b, double *c, int n){

    int i,j,k;

    for (i=0; i<n; i++){
        for (j=0; j<n; j++){
            for (k=0; k<n; k++){
                c[i*n+j] += a[i*n+k] * b[k*n+j]; // multiply row a by column b
            }
        }
    }
}


// matrix power function

void power(double *a, int n, int p){
    int i,j,k;

    double *a0, *ai;

    a0 = (double *)malloc(sizeof(double)*N*N);
    ai = (double *)malloc(sizeof(double)*N*N);

    for (i=0; i<n; i++){
        for (j=0; j<n; j++){
            a0[i*n+j] = a[i*n+j]; // creating a replica 'a' of 'a0' to then multiply it by itself
        }
    }

    for (k=1; k<p; k++){

         multiply(a0,a,ai,n);

         for (i=0; i<n; i++){
            for (j=0; j<n; j++){
                a[i*n+j]=ai[i*n+j]; // allocates a as a*a to then pass to multiply again for a*a*a and so on
            }
         }
    } 
}



void print(double *a, int n){

    int i,j;

    for (i=0; i<n; i++){
        printf("| ");
        for (j=0; j<n; j++){
            printf("%4.1f ",a[i*n+j]);
        }
        printf("|\n");
    }
    printf("\n");
}

int main(){

    int i;
    double *a, *b, *c;

    a = (double *)malloc(sizeof(double)*N*N);
    b = (double *)malloc(sizeof(double)*N*N);
    c = (double *)malloc(sizeof(double)*N*N);

    a[0*N+0] = 1.0;
    a[0*N+1] = -1.0;
    a[1*N+0] = 1.0;
    a[1*N+1] = 1.0;

    b[0*N+0] = 0.5;
    b[0*N+1] = 0.5;
    b[1*N+0] = -0.5;
    b[1*N+1] = 0.5;

    multiply(a,b,c,N);
    print(c, N);

    power(a,N,3);
    print(a,N);

    free((void *) a);
    free((void *) b);
    free((void *) c);


    return 0;
}
