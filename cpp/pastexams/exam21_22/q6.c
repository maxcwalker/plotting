#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define Ti 0.0 // initial time
#define Tf 50.0 // final time
#define dT 0.001 // time step

#define Y01 0.0 // initial condition 1
#define Y02 1.0 // initial condition 2
#define Y03 0.0 // initial condition 3

#define sigma 10.0 // Lorenz equations parameters
#define b 8.0/3.0 
#define r 28.0


void lorenz(double *y, double *f){
    f[0] = sigma * (y[1]-y[0]);
    f[1] = r*y[0] - y[1] - y[0]*y[2];
    f[2] = y[0]*y[1] - b*y[2];
}

void euler(double **y, void (*f)(double*, double*), int n){
    int i;
    double yin[3], yout[3];

    y[0][0] = Y01;
    y[1][0] = Y02;
    y[2][0] = Y03;

    for (i=0; i<n; i++){
        yin[0] = y[0][i];
        yin[1] = y[1][i];
        yin[2] = y[2][i];

        f(yin,yout);

        y[0][i+1] = y[0][i] +dT*yout[0];
        y[1][i+1] = y[1][i] +dT*yout[1];
        y[2][i+1] = y[2][i] +dT*yout[2];
    }
}

int main(){
    int i, N;
    FILE *fw;
    double *t, **y;
    N = (int) (Tf - Ti) / dT;

    t = (double *)malloc(sizeof(double)*(N+1));

    y = (double **)malloc(sizeof(double)*3);
    for (i=0; i<3; i++){
        y[i] = (double *)malloc(sizeof(double)*(N+1));
    }

    //open file data.txt for writing
    if ((fw = fopen("data.txt","wr"))==NULL){
        printf("Cannot open dile data.txt for writing");
        return -1;
    }
    for (i=0; i<=N; i++){
        t[i] = Ti +dT*i; // define time 
    }

    // solve the ODE system
    euler(y, lorenz, N); // y to store the solution

    //print to file
    for (i=0; i<=N; i++){
        fprintf(fw,"%f\t%f\t%f\t%f\n",t[i],y[0][i],y[1][i],y[2][i]);
    }
    //close files
    if (fclose(fw) != 0){
        printf("The file could not be closed");
        return -1;
    }

    // free the arrays
    free((void *) t);

    for (i=0; i<3; i++){
        free((void *)y[i]);
    }
    free((void **) y);

    return 0;
}