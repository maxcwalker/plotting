
/* This script demonstrates pointers in strunctures and different syntax */

#include<stdio.h>

typedef struct{
    float re;
    float im;
}complex;

int main(){
    complex v={0.0, 1.0};
    complex *u=&v;

    printf("%.1f + %.1fj\n",v.re,v.im);
    printf("%.1f + %.1fj\n",(*u).re,(*u).im);
    printf("%.1f + %.1fj\n",u->re,u->im);

    return 0;
}
