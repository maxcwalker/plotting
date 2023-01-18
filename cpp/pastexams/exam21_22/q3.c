#include<stdio.h>
#include<math.h>
#include<stdlib.h>

/* a. Write the function header for a function called exchange that takes two pointers to double-precision,
floating-point numbers x and y as parameters and does not return a value. */

void exchange(double x, double y)

/* b. Write the function prototype for the function in part (a). */

double exchange(double x, double y)
// only showing what it would look like 
{
int temp=*x;
*x=*y;
*y=temp;
}

/* c. Write the function header for a function called evaluate that returns an integer and that takes as parameters 
integer x and a pointer to function poly. Function poly takes an integer parameter and returns an integer. */

int evaluate(int x,  int (*poly)(int))

/* d. Write the function prototype for the function in part (3). */
void exchange(int* x,int* y)

/* 5. Write a declaration for integer count that should be maintained in a register. Initialise count to 0. */
register int count =0;

/* 6) Write the statement to show how to assign the address of a float value called radius to a pointer.  */
float radius;
float *ptr;
ptr = &radius;

/* 7) Write the statement that would declare a 5-element integer array and initialise all its elements to 1. */
nt arr[] = {1,1,1,1,1};

/* 8) Write a line of code that declares an array of type char, and initialise it to the string “pointers are fun!”. 
Make the array just large enough to hold the string. */
char s[] = "pointers are fun!";

/* 9) Write a line of code that allocates storage for the string “pointers are fun!”, as in part (8), but without using an array. */

size = 6; //length of string
str = (char *)malloc(sizeof(char)*size)

/* 10) Write a prototype for a function called numbers that takes three integer arguments. The integers should be passed by reference.
*/
int numbers(&x, &y, &z);

int main(){
    i
    return 0;
}

