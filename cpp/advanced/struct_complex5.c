
/* Explores the use of malloc */

#include<stdio.h>
#include<stdlib.h>

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

int main()
{
    complex v = {0.0, 1.0};
    complex u = {1.0, 0.0};
    complex w, *z;

    w = add(&v, &u);
    printf("a) %f + %fj\n",w.re,w.im);

    // as z is an address however does not have storage allocated, it must be done before calling the values of *z
    z = (complex *)malloc(sizeof(complex)); 

    *z = add(&v, &u);
    printf("b) %f + %fj\n",z->re,z->im);

    free((void *) z);

    return 0;
}