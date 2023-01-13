#include<stdio.h>
int main(void)
{
    int c;
    for(c=32; c<127; c++)
    {
        printf("%3d : %c\n",c,c);
    }
    return 0;
}