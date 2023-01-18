#include<stdio.h>

/* function prototype */
//long string_length(char s[]);

int string_length()
{
    char c;
    int nc = 0;// number of characters
    while (s != '\0')
    {
        nc++;
    }
    return nc;
}

int main(void){
    char s1[] = "Hello";
    char s2[] = "X";
    char s3[] = "line1\tline2\n";

    printf("%20s | %s\n", "string_length(s)", "s");
    printf("%20ld | %s\n", string_length(s1), s1);
    printf("%20ld | %s\n", string_length(s2), s2);
    printf("%20ld | %s\n", string_length(s3), s3);
    return 0;
}