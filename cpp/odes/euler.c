
/* 
function Euler implements Euler method for solving first order ODEs dy/dt = f(t,y).

Input parameters are:
t - independant variable (time) given as 1D array
y - dependant variable given as 1D array
y0 - initial conditions
f - pointer to a founction to be integrated
n - the length of arrays t and y (must be the same length)

The solution is stores in the array y.
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define Ti 0.0 // initial time
#define Tf 2.0 // final time step
#define dT 0.4 // time step
#define Y0 0.0 // initial condition

// ------------------------------------------------------------------------------//
// ------------------------------------------------------------------------------//


void euler( double *t, double *y, double y0, double (*f)(double, double), int n)
{
    int i;
    float dt = t[1] - t[0]; // step

    y[0] = y0;
    for (i=0; i<n; i++){
        y[i+1] = y[i] + dt*f(t[i],y[i]); 
    }
}

/*
Functipon rk2 implements second order Runge-Kutta method for solving first order ODEs dy/dt = f(t,y).

Input parameters:
t - independant variable (time) given as 1D array
y - dependant variable given as 1D array
y0 - initial conditions
f - pointer to a founction to be integrated
n - the length of arrays t and y (must be the same length)

The solution is stores in the array y.
*/

void rk2( double *t, double *y, double y0, double (*f)(double, double), int n)
{

    float dt = t[1] - t[0];
    float k1,k2,k3,k4;

    y[0] = y0;
    for (int i=0; i<n; i++)
    {
        k1 = dt * f(t[i], y[i]);
        k2 = dt * f(t[i]+dt/2.0, y[i] +k1/2.0);

        y[i+1] = y[i] + k2;
    }
}

/*
Right hand side function f of ODE:

dy/dt = f(t, y)

where:

f(t, y) = -t * (1.0 + y)^2

The input variables t and y are assumed to be scalars.
*/

double fode(double t, double y)
{
    return -t * (1.0 + y) * (1.0 + y);
}

int main()
{
    int i;
    int N;

    FILE *fw;
    double *t, *y_e, *y_rk;
    N = (int) (Tf - Ti) / dT;

    // allocate array momory (must be N + 1 to include T0 and Tf).
    t = (double *)malloc(sizeof(double)*(N+1));
    y_e = (double *)malloc(sizeof(double)*(N+1));
    y_rk = (double *)malloc(sizeof(double)*(N+1));

    // open file data.txt for writing
    if ((fw=fopen("data.txt","w"))==NULL)
    {
        printf("Cannot open 'data.txt for writing.\n");
        return -1;
    }

    for (i=0; i<=N; i++)
    {
        t[i] = Ti +dT*i; // like linspace in numpy
    }

    euler(t, y_e, Y0, fode, N); // y_e to store solution
    rk2(t, y_rk, Y0, fode, N); // y_rk to store solution

    // print to the file
    for (i=0; i<=N; i++)
    {
        fprintf(fw,"%f\t%f\t%f\n",t[i], y_e[i], y_rk[i]);
    }

    if (fclose(fw) != 0)
    {
        printf("The file could not be closed.\n");
        return -1;
    }

    free((void *) t);
    free((void *) y_e);
    free((void *) y_rk);

    return 0;
}