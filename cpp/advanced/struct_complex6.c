#include<stdio.h>
#include<stdlib.h>

typedef struct{
    double *re;
    double *im;
}complex;

int main()
{
    complex a,b;
    double x,y;

    x = 1.0;
    y = 2.0;

    // we can treat the structure members (*re and *im) as normal pointers
    a.re = &x;
    a.im = &y;
    printf("The complex number is %.1f + %.1fj\n",*a.re,*a.im);

    /* setting up the structure member arrays using dynamic memory allocation. 
    for example, arrays of length 2 */

    b.re = (double *)malloc(2*sizeof(double));
    b.im = (double *)malloc(2*sizeof(double));

    b.re[0] = 1.0;
    b.re[1] = 2.0;
    *b.im = -1.0;
    *(b.im+1) = -2.0;

    printf("The complex number is %.1f + %.1fj\n",*b.re,*b.im);
    printf("The complex number is %.1f + %.1fj\n",*(b.re+1),*(b.im+1));

    free((void *) b.re);
    free((void *) b.im);

    return 0;
}