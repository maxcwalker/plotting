#include<stdio.h>

int main(){
    int num=5; 
    int *ptr;
    ptr = &num; // ptr now points at the address of num

    printf("%d\n", ptr);
    printf("%d\n", *ptr);

    return 0;
}