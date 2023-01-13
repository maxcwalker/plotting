#include<stdio.h>

struct complex{
    double re;
    double im;
};

struct complex add(struct complex a, struct complex b){

    struct complex c;
    
    c.re = a.re + b.re;
    c.im = a.im + b.im;

    return c;
};

int main(void){
    struct complex v = {4.0, 2.0};
    struct complex u = {1.0, 1.0};
    struct complex w;

    w = add(v,u);
    printf("%.2f + %.2fj\n",w.re,w.im);
    return 0;
}