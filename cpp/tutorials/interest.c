#include<stdio.h>

int main()
{
    double s = 1000; // interest
    double debt = s; // actual debt
    double rate = 0.03; // interest rate
    int month;
    double time = 12; // how many months over
    double interest;
    for(month=0; month < time; month++)
    {
        interest = (debt*rate);
        debt = debt + interest;

        printf("month %2d : debt = £%7.2f, interest = £%.2f\n",month, debt, interest);
    }
    return 0;

}