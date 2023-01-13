#include<stdio.h>

int main(void){
    int nc, nl, nw;
    char c;
    nc = nl = nw = 0;
    while((c=getchar()) != EOF){
        nc++;
        if (c=='\n'){
            nl++;
        }
        if (c == '\n' || c == ' ' || c == '\t'){
            nw++;
        }
    }
    printf("characters lines words\n");
    printf("%10d%6d%6d\n",nc,nl,nw);
    return 0;
}