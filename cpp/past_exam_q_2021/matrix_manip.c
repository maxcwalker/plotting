#include<stdio.h>

struct print_matrix(int a,int b,int c,int d){
    printf("%d\t%d\n",a,b);
    printf("%d\t%d\n",c,d);
};

int main(void){
    struct print_matrix a={1,0,0,1};
    return 0;
}
