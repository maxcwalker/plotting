#include<stdio.h>
#include<string.h>

int main(void){
    char c[]="Hello World";
    int i=0;

    for (i=0; i<strlen(c); i++){
        printf("%c", c[i]);
    }

    for (i=0; i<strlen(c); i++){
        printf("%c", *(c+i));
        
    } 
    printf("\n");

    int strlen = 0;
    int j = 0;

    while (c[j] != '\0'){
        strlen++;
        j++;
    }
    
    printf("The string is %d characters long\n",strlen);

    return 0;
}