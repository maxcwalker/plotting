#include<stdio.h>



// by using typedef we can stop using "struct complex" and just use "complex" 
typedef struct{
    double re;
    double im;
}complex; // have to put the name of the struture at the end of the bracket

complex add(complex a, complex b){
    complex c;
    c.re = a.re + b.re;
    c.im = a.im + b.im;

    return c;
};

int main(){
    complex v = {1.0, 0.0};
    complex u = {2.0, 1.0};

    complex w;
    w = add(v,u);
    printf("%.1f + %.1fj\n",w.re,w.im);
}