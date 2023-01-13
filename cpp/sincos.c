#include<stdio.h>
#include<math.h>

double sinx(double x)
{
    double sinx;
    sinx = sin(x);
    return sinx;
}

double cosx(double x)
{
    double cosx;
    cosx = cos(x);
    return cosx;
}

int main()
{
    double i;
    double n = 10; //number to go up to
    printf("  x  |   sin(x)   |   cos(x)\n");
    printf("----------------------------\n");
    for (i=0; i<n; i++)
    {  
        double sini = sinx(i/10);
        double cosi = cosx(i/10);
        printf("%.1f  |  %f  |  %f  \n", i/10, sini,cosi);
    }
    return 0;
}