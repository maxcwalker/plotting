#include <stdio.h> 
int main(void) {
    int x=1, y=2;
    int *pi;
    pi=&x;
    y=*pi;
    *pi=0;
    pi=&y;
    printf("x=%d, y=%d \n",x,y); 
    printf("address x=%p, address y=%p \n", (void *) &x, (void *) &y );
     printf("pi=%p, *pi=%d \n",(void *) pi,*pi);

    return 0;
}