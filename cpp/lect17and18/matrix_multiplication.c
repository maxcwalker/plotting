#include<stdio.h>
#define N 3

int main(){
    int i,j,k;

    int m[N][N] = {{1,2,3},{2,3,4},{3,4,5}};
    int n[N][N] = {{3,2,1},{4,3,2},{5,4,3}};
    int o[N][N] = {{0,0,0},{0,0,0},{0,0,0}};

    for (i=0; i<N; i++){
        for (j=0; j<N; j++){
            for (k=0; k<N; k++){
                o[i][j] = m[i][k] + n[k][j];
            }
        }
    }
    printf("\n");
    printf("The Matrix m x n is:\n");
    printf("%2d %2d %2d\n",o[0][0],o[0][1],o[0][2]);
    printf("%2d %2d %2d\n",o[1][0],o[1][1],o[1][2]);
    printf("%2d %2d %2d\n",o[2][0],o[2][1],o[2][2]);
    printf("\n");

    return 0;
}