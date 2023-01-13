#include<stdio.h>

void print_array1(int a[]){
    int i;
    for (i=0; i<5; i++){
        printf("%d\t",a[i]);
    }
    printf("\n");
}

void print_array2(int *a){
    int i;
    for (i=0; i<5; i++){
        printf("%d\t",a[i]);
    }
    printf("\n");
}

int main(){
    int a[5];
    int i;
    for (i=0; i<5; i++){
        a[i] = i*i;
    }
    print_array1(a);
    print_array2(a);

    return 0;
}

