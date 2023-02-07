#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define Ti 0.0 // start time
#define Tf 30.0 // end time
#define dT 0.001 // time step

#define Y01 70.0 // initial condition 1
#define Y02 50.0  // initial condition 2

#define A 0.7 // rabbit birth rate
#define C 0.007 // Rabbit-fox collision rate
#define B 1 // fox death rate


void fode2(double *p, double *f){
    f[0] = A*p[0] - C*p[0]*p[1];
    f[1] = C*p[0]*p[1] - B*p[1];
}

void euler(double *y1, double *y2, void (*f)(double *, double *),int n){

    double out[2], p[2];

    y1[0] = Y01;
    y2[0] = Y02;
    double dt = (Tf-Ti) / dT;

    for(int i=0; i<n;i++){
        p[0] = y1[i];
        p[1] = y2[i];

        f(p,out);
        y1[i+1] = y1[i] + dt * out[0];
        y2[i+1] = y2[i] + dt * out[1];
    }
}

int main(){

    FILE *fw;
    // ...
    // ...

    int N = (Tf-Ti) / dT;

    double *y1, *y2, *t;
    y1 = (double *)malloc(sizeof(double)*(N+1));
    y2 = (double *)malloc(sizeof(double)*(N+1));
    t = (double *)malloc(sizeof(double)*(N+1));

    euler(y1, y2, fode2, N); // y1 & y2 to store the solutions

    // no explicity time dependance

    // print to file
    if ((fw = fopen("data.txt","wr"))==NULL){
        printf("Cannot open file data.txt for writing");
        return -1;
    }
    for (int i=0; i<=N; i++){
        t[i] = Ti +dT*i; // define time for the file, not for calcs!
    }

    //print to file
    for (int i=0; i<=N; i++){
        fprintf(fw,"%.2f\t%.2f\t%.2f\n",t[i],y1[i],y2[i]);
    }

    //close files
    if (fclose(fw) != 0){
        printf("The file could not be closed");
        return -1;
    }

    // ...
    // ...
}