#include <stdio.h>

int main(void){
    double x = 1;
    
    while(x<50){
        printf("This iteration is %f\n",x);
        x = x * 1.5;
    }
    return 0;
}