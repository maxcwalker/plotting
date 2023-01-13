#include<stdio.h>

void swap(int *x, int *y){
    int tmp;
    tmp = *x;
    *x = *y;
    *y = tmp;
}

int main(void){
    int a=1,b=2;

    printf("Before the swap a=%d and b=%d\n",a,b);
    swap(&a,&b);
    printf("After the swap a=%d and b=%d\n",a,b);
}