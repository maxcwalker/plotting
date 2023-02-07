/*
FEEG6002 exam 2022-2023
Question 3

Please write your solutions to Question 3
below and submit this file as Q3.c when ready.
*/
#include<stdio.h>
#include<stdlib.h>
#define MAXLEN 100

typedef struct{
    char country[MAXLEN];
    char language[MAXLEN];
    char opsys[MAXLEN];
}data;

int num_lines(char s[]){
    FILE *f;

    int counter = 0;

    if ((f = fopen(s,"r")) == NULL){
        printf("Cannot open %s for reading.\n",s);
        return -1;
    }
    char c;

    int nl = 0; //line count

    while((c=fgetc(f)) != EOF){
        if (c == '\n'){
            nl++;
        }
    }
    return nl;
}

int string_in(char s1[], char s2[]){
    int i =0;
    char c;

    int s2_len = 0;

    if (s2[i] != '\0'){
        i++;
    }
    int k=0;

    for (int j=0; j<MAXLEN; j++){
        if (s1[j] == s2[k]){
            k++;
        }
    }


    if (k == i){
        return 1;
    }
    else{
        return 0;
    }
}

void build_database(char s[], data *dbs, int n){
    // n is the size of the array dbs
    FILE *f;

    if ((f = fopen(s,"r")) == NULL){
        printf("Cannot open %s for reading.\n",s);
    }

    int x1;
    char x2[MAXLEN],x3[MAXLEN],x4[MAXLEN],x5[MAXLEN];

    while(fscanf(f,"%d,%s,%s,%s,%s\n", x1, x2, x3, x4, x5)==5){
            //printf("%s\t%d\t%d\t%d\t%d\n", x1, x2, x3, x4, x5);

            for (int i=0; i<MAXLEN; i++){
                if ((x3[i]) != '\0'){
                    dbs->country[i] = x3[i];
                }
            }
            
            for (int i=0; i<MAXLEN; i++){
                if ((x4[i]) != '\0'){
                    dbs->language[i] = x4[i];
                }
            }

            for (int i=0; i<MAXLEN; i++){
                if ((x5[i]) != '\0'){
                    dbs->opsys[i] = x5[i];
                }
            }
        }
}


void find_percent(double perc[3],data *dbs, nl){

    int C_users = 0;
    double C_users_perc;
    for (int i=0; i<nl; i++){
        for(int j=0; j<MAXLEN; j++){
            if (dbs[i].language[j] == 'C' && dbs[i].language[j+1] == ';'){
                C_users++;
            }
        }         
    }
    C_user_perc = (C_users / nl) *100.0;

    for (int i = 0; i<nl; i++){
        for (int j=0; j<MAXLEN; j++){
            if (dbs[i].language[0] =='U' && dbs[i].language[7] == 'K'){
                
            }
        }
    }

}



int main(){
    char filename[] = "survey_results_public_short.csv";

    int nl = num_lines(filename);

    //int string_in(...);

    data *dbs;
    dbs = (data *)malloc(sizeof(data)*nl);
    
    build_database(filename, dbs,nl);

    for (int i=0; i<nl; i++){
        printf("%s",dbs[i].opsys);
    }


    return 0;
}