
/* This script demonstrates the use of functions within the structures 
mainly some more pointer stuff */

#include<stdio.h>

typedef struct{
    float re;
    float im;
} complex;

complex add(complex *a, complex *b){
    complex c;

    c.re = a->re + b->re;
    c.im = a->im + b->im;

    return c;
};

int main(){
    complex v = {1.0, 2.0};
    complex u = {3.0, 4.0};

    complex w;

    w = add(&v, &u);
    printf("%.1f + %.1fj\n",w.re,w.im);
    return 0;
}


