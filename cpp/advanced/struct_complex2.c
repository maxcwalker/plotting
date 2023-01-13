#include<stdio.h>
#define N 3

typedef struct{
    float re;
    float im;
}complex;

complex add(complex a, complex b){

    complex c;

    c.re = a.re + b.re;
    c.im = a.im + b.im;

    return c;
};

int main(){
    complex a[N] = {{3.0,1.0},{5.0,-1.0},{-1.0,1.0}};
    complex s = {0.0,0.0};
    int i;
    for (i=0; i<N; i++){
        s = add(s,a[i]);
    }
    printf("%.1f + %.1fj\n",s.re,s.im);

    return 0;
}