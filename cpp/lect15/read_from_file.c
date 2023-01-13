#include<stdio.h>
#include<stdlib.h>

int main(){
    FILE *f;
    char c;
    if ((f=fopen("myfile.txt","r"))==NULL){
        printf("Cannot open the file for reading");
        return -1;
    }

    /* read from the file, character by character */
    while ((c=fgetc(f)) != EOF){
        printf("%c",c);
    }
    
    if (fclose(f) != 0){
        printf("File could not be closed.\n");
        return 0;
    }
    return 0;
}