#include<stdio.h>
#include<stdlib.h>
#include<math.h>

typedef struct{
    char state[15]; // state name
    long dempv; // democrats popular votes
    long demev; // democrats electoral votes
    long reppv; // republicans popular votesv
    long repev; // republicans electoral votes
}votes;

int count_lines(char s[]){
    FILE *f;

    int counter = 0;

    if ((f = fopen(s,"r")) == NULL){
        printf("Cannot open %s for reading.\n",s);
        return -1;
    }
    char x1[15];
    long x2,x3,x4,x5;
    while (fscanf(f,"%s\t%lf\t%lf\t%lf\t%lf",&x1, &x2, &x3, &x4, &x5) == 5){
        counter++;
    }
    
    return counter;
}

////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////

void initialise_votes(char s[],votes arr , int n){
    FILE *f;
    if ((f = fopen(s,"r")) == NULL){
        printf("Cannot open %s for reading.\n",s);
    }

    // votes *arr
    // arr = (votes *)malloc(sizeof(votes)*n);
    char x1[15];
    long x2,x3,x4,x5;
    int i=0;

    while (fscanf(f, "%s\t%lf\t%lf\t%lf\t%lf", &arr.state, &arr.dempv, &arr.demev, &arr.reppv, &arr.repev) == 5){
        i++;
    }
}

////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////

int main(){
    
    char filename[] = "data.txt";
    int nlines = count_lines(filename);
    
    printf("%d\n",nlines);

    votes **arr;
    arr = (votes **)malloc(sizeof(votes *));
    //for (int i=0; i<nlines; i++){
    //     arr[i] = (votes *)malloc(sizeof(votes));
    // }

    initialise_votes(filename,&arr,nlines);

    printf("%s",arr->state[0]);
}