#include<stdio.h>
#define LOWER -30
#define UPPER 30
#define STEP 2

int main(){
    double cels;
    printf("\n");
    printf("---------------------\n");
    printf("|cels\t| fahrenheit|\n");
    printf("|-------------------|\n");
    for (cels=LOWER; cels<UPPER; cels+=STEP){
        double farh = cels*(9.0/5.0)+32.0;
        printf("|%4.0f\t| %6.1f    |\n",cels,farh);
    }
    printf("---------------------\n");
    printf("\n");

    return 0;
}