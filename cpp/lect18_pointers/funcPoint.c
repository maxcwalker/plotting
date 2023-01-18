#include<stdio.h>

void fun(int a){

    printf("\n");
    printf("Value of a is %d.\n",a);
    printf("\n");

}

void add(int a, int b){
    printf("Addition is %d\n",a+b);
}

void subtract(int a, int b){
    printf("Subtraction is %d\n",a-b);
}

void multiply(int a, int b){
    printf("Multiplication is %d\n",a*b);
}


// int main(){

//     // fun_ptr is pointing to the function fun
//     void (*fun_ptr)(int) = &fun;

//     (*fun_ptr)(10);

//     return 0;
// }


// int main(){

//     void (*fun_ptr)(int) = fun;
//     fun_ptr(10);

//     return 0;
    
// }


int main(){
    void (*fun_ptr_arr[])(int, int) = {add, subtract, multiply};
    unsigned int ch, a = 15, b = 10;

    printf("Enter Choice: 0 for add, 1 for subtract, 2 for multiply.\n");

    scanf("%d",&ch);

    if (ch>2){
        return 0;
    }

    (*fun_ptr_arr[ch])(a,b);
    return 0;
}
