#include<stdio.h>
#include<stdlib.h>
#include<math.h>

typedef struct{
    char state[100]; // state name
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

void initialise_votes(char s[], votes *arr, int n){
    FILE *f;
    if ((f = fopen(s,"r")) == NULL){
        printf("Cannot open %s for reading.\n",s);
    }

    // this is where the problem is
    char x1[100];
    
    int x2,x3,x4,x5;

        while(fscanf(f,"%s\t%d\t%d\t%d\t%d\n", x1, &x2, &x3, &x4, &x5)==5){
            //printf("%s\t%d\t%d\t%d\t%d\n", x1, x2, x3, x4, x5);

            for (int i=0; i<20; i++){
                if ((x1[i]) != '\0'){
                    arr->state[i] = x1[i];
                }
            }
            arr->dempv = x2;
            arr->demev = x3;
            arr->reppv = x4;
            arr->repev = x5;
            arr++;
        }
}

////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////

void print_list(votes *arr, int n){
    for (int i=0; i<n; i++){
        printf("%s\t%d\t%d\t%d\t%d\n",(arr+i)->state,(arr+i)->dempv,(arr+i)->demev,(arr+i)->reppv,(arr+i)->repev);

    }
}

////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////


votes print_vote_state(votes *arr, int n){
    // 2 dempv and 4 repve are the popular votes fyi

    int total[n];

    for (int i=0; i<n; i++){
        total[i] = (arr+i)->dempv + (arr+i)->reppv;
        printf("%d\n",total[i]);
    }

    int maxv = 0;
    int f = 0;
    for (int i=0; i<n; i++){
        if(total[i] > maxv){
            maxv = i;

        }
    }
   
   votes ret;
   for (int i=0; i<15; i++){
    ret.state[i] = (arr+maxv)->state[i];
   }
   ret.dempv = (arr+maxv)->dempv;
   ret.demev = (arr+maxv)->demev;
   ret.reppv = (arr+maxv)->reppv;
   ret.repev = (arr+maxv)->repev;

   return ret;
}




////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////

int main(){
    char filename[] = "data.txt";
    int nlines = count_lines(filename); // get number of lines in the data

    votes *arr;

    for (int i=0; i<nlines; i++){
        // printf("votes array, ");
        arr = (votes *) malloc(sizeof(votes));
        arr++;
    }
    arr = (votes *) malloc(sizeof(votes)*nlines); // allocate the necessary momory

    initialise_votes(filename,arr,nlines);

    print_list(arr,nlines);

    votes maxstate = print_vote_state(arr, nlines);

    //printf("%s\n", maxstate.state);
}
