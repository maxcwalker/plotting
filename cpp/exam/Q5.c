/*
FEEG6002 exam 2022-2023
Question 5

Please write your solutions to Question 5
below and submit this file as Q5.c when ready.
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define M 1.0
#define C 1.0
#define K 1.0
#define G 10.0

#define Ti 0.0
#define Tf 5.0
#define dT 0.1

#define X0 1.0
#define V0 0.0


void osclin(double *a, double *b){
    b[0] = a[1];
    b[1] = (-C / M) * a[1] - (K / M) *a[0] +G;
}


void oscnonl(double *a, double *b){
    b[0] = a[1];
    b[1] = (-C / M) * a[1] - (K / M) * (a[0]*a[0]*a[0]) + G;
}


void euler(double **p, void (*f)(double *, double *),int n){

    double out[2], in[2];

    p[0][0] = X0;
    p[0][1] = V0;

    double dt = 0.1;

    for(int i=0; i<n; i++){
        in[0] = p[0][i];
        in[1] = p[1][i];

        f(in,out);

        p[0][i+1] = p[0][i] + dt * out[0];
        p[1][i+1] = p[1][i] + dt * out[1];
    }
}

void diff(double **p, int n, void (*f1)(double *, double *), void (*f2)(double *, double *)){
    double **osclin, **oscnonl;
    osclin = (double **)malloc(sizeof(double *)*2);
    osclin[0] = (double *)malloc(sizeof(double)*n);
    osclin[1] = (double *)malloc(sizeof(double)*n);

    oscnonl = (double **)malloc(sizeof(double *)*2);
    oscnonl[0] = (double *)malloc(sizeof(double)*n);
    oscnonl[1] = (double *)malloc(sizeof(double)*n);

    euler(osclin,f1, n);
    euler(oscnonl,f2, n);

    for (int i=0; i<n; i++){
        p[0][i] = osclin[0][i] - oscnonl[0][i];
        p[1][i] = osclin[1][i] - oscnonl[1][i];
    }
}

int main(){

    FILE *fw;
    int N = (Tf-Ti) / dT;

    double **p, *t;
    p = (double **)malloc(sizeof(double *)*2);
    p[0] = (double *)malloc(sizeof(double)*N);
    p[1] = (double *)malloc(sizeof(double)*N);
    t = (double *)malloc(sizeof(double)*N);

    for (int i=0; i<N; i++){
        t[i] = Ti *dT*i;
    }

    diff(p,N,osclin, oscnonl);
    
    if ((fw = fopen("data.txt","wr"))==NULL){
        printf("Cannot open file data.txt for writing");
        return -1;
    }

    //print to file
    for (int i=0; i<=N; i++){
        fprintf(fw,"%f\t%f\t%f\n",t[i],p[0][i],p[1][i]);
    }

    //close files
    if (fclose(fw) != 0){
        printf("The file could not be closed");
        return -1;
    }

    return 0;
}