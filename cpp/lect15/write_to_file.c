#include<stdio.h>
int main(void){
    FILE *f; // A pointer to the file
    if ((f=fopen("myfile.txt","w"))==NULL){
        printf("File cannot be opened");
        return -1;
    }
    fprintf(f,"We can now print to the file f using fprintf\n");
    fprintf(f,"For example, a number %d and %d and %d.\n",1, 2, 42);

    if (fclose(f)!=0){
        fprintf(f,"File could not be closed.\n");
        return -1;
    }
    return 0;
}