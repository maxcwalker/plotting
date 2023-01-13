#include<stdio.h>

int main()
{
    char c;
    while ((c=getchar())!=EOF)
    {
        putchar(c);
    }
    fprintf(stderr,"Goodbye all.\n");
    return 0;
}