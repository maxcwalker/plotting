#include<stdio.h>

struct person{
    int age;
    double height;
    double weight;
};

int main(void){
    struct person Max={25,1.75,85.0};
    printf("Max's age: %d\n", Max.age);
    printf("Max's height: %.2lf\n", Max.height);
    printf("Max's weight: %.1lf\n", Max.weight);

    return 0;
}