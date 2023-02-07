/*
FEEG6002 exam 2022-2023
Question 4

Please write your solutions to Question 4
below and submit this file as Q4.c when ready.
*/
#include<stdlib.h>
#include<stdio.h>
#include<math.h>

#define ftol 0.000001


double bisect(double (*f)(double), double a, double b, int maxint){
    

    double x = 0;
    int x_num = 0;

    while (abs(f(x)) > ftol){
        if (f(x)*f(a) > 0){
            a = x;
        }
        else{
            b = x;
        }
        x = (a+b) / 2;

        x += 0.01;
        x_num++;
        

    }

    if (x_num > maxint){
        x = 0.0/0.0;
    }

    return x;
}

double newton(double (*f)(double), double x0, int maxint){

    double dx = 0.0001;
    double x;

    
    while (abs(f(x)) > ftol){
        for (int i = 0; i<maxint; i++){
            if (i >= maxint){
                return 0.0/0.0;
            }
            else{
            x = dx * i;
            double dfdx = (f(x+dx) - f(x)) / dx;

            x = x - f(x) / dfdx;
            
            }
    }
    return x;
    }
}

double parab(double x){
    return x*x -1.0;
}

double cosxx(double x){

    double y = cos(x) - 1;
    return y;
}

int main(){

    printf("bisect(parab) root 1: %lf\n", bisect(parab, -2, 0, 50));
    printf("bisect(parab) root 2: %lf\n", bisect(parab, 0, 2, 50));
    printf("newton(parab) root 1: %lf\n", newton(parab, -2, 50));
    printf("newton(parab) root 2: %lf\n", newton(parab, 2, 50));
    // find both roots of function sinxx
    // using bisection and newton methods
    printf("bisect(cosxx) root 1: %lf\n", bisect(cosxx, -2, 0, 50));
    printf("bisect(cosxx) root 2: %lf\n", bisect(cosxx, 0, 2, 50));
    printf("newton(cosxx) root 1: %lf\n", newton(cosxx, -2, 50));
    printf("newton(cosxx) root 2: %lf\n", newton(cosxx, 2, 50));
    double x = cosxx(5);
    return 0;
}




