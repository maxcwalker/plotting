#include<stdio.h>

struct person{
    int age;
    double height;
    double weight;
    char name[10];
};

void printDetails(struct person A){
    printf("The age is %d\n",A.age);
    printf("The height is %.2lf\n",A.height);
    printf("The weight is %.2lf\n",A.weight);
    printf("The name is %s\n",A.name);
}

int main(void){
    struct person Max={25,179.63,85.4,"Max"};
    printDetails(Max);

    return 0;
}
