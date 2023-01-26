#include<stdio.h>
#include<stdlib.h>


double trapez(double (*fun)(double), double a, double b, int n){
    int i;
    double A,h,x;

    h = (b-a) / n;
    A = fun(a);

    for (i=0;i<n-1;i++){
        x = a + i*h;
        A += 2.0*fun(x);
    }
    A += fun(b);
    return A*h / 2.0;
}

double error_trapez(double (*f)(double), double (*fint_an)(double, double), double a, double b, int n){
    double Ian, Itrapez;
    Ian = fint_an(a,b);
    Itrapez = trapez(f, a, b, n);
    return Itrapez - Ian;
}

double qgaus(double (*func)(double), double a, double b){
    int j;
    double xr, xm, dx, s;
    double x[] = {0.0, 0.1488743389, 0.4333953941,
        0.6794095682, 0.8650633666, 0.9739065285};
    double w[] = {0.0, 0.2955242247, 0.2692667193,
        0.2190863625, 0.1494513491, 0.0666713443};
    /* The first value of arrays x, w is not used. */
    xm = 0.5 * (b + a);
    xr = 0.5 * (b - a); s=0;
    for (j =1;j<=5;j++) {
        dx =xr*x[j];
        s += w[j] * ((*func)(xm + dx) + (*func)(xm - dx));
    }
    return s *= xr;
}

double error_qgaus(double (*fun)(double), double (*fint_an)(double, double),double a, double b){
    double Ian, Iqgaus;
    Ian = fint_an(a,b);
    Iqgaus = qgaus(fun,a,b);

    return Iqgaus - Ian;
}

double f(double x){
    return x*x;
}

double If_an(double a, double b){
    return b*b*b/3.0 - a*a*a/3.0; 
}

int main(void){
    double A,diff,a,b;
    int n;
    a = -1.0; b=2.0; n=10;
    A = trapez(f,a,b,n);
    printf("A_trapez = %f.\n", A);
    A = qgaus(f,a,b);
    printf("A_qgaus = %f\n", A);
    diff = error_trapez(f,If_an,a,b,n);
    printf("Diff_trapez = %f\n",diff);
    diff = error_qgaus(f,If_an,a,b);
    printf("Diff_qgaus = %f\n",diff);

    getchar();
    return 0;
}