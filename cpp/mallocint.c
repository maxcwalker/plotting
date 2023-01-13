#include<stdio.h>
#include<stdlib.h> //provides the malloc

/* malloc function allocates the requested memory and 
returns the address of that memory */
int main(void){

    int *pi;

    // Malloc allocates on a heap; Not consecutive allocation.

    pi = (int *)malloc(sizeof(int)); //(int *) tells it what type to return it as - integer.
    // pi = (double *)malloc(10*sizeof(double)); This one allocates the memory size of 10 doubles - just fyi

    /* This doesnt really apply these days with the size of memory available but if there isn't enough
    memory to allocate the requested amount then it will return NULL */
    if (pi == NULL){
        print("ERROR: Out of memory\n");
        return 1;
    }
    /* as the momory has been allocated, *pi can be changed to an integer (5) */

    *pi = 5;
    print("%d\n",*pi);

    free(pi); // Frees the momory used 

    return 0;
}