#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define PI 3.141;

typedef struct{
    double x1;
    double x2;
    double x3;
}lines;

int number_of_lines(char s[]){
    FILE *f;

    if ((f=fopen(s, "r")) == NULL){
        printf("The file %s cannot be opened for reading.\n",s);
    }

    int nl = 0;
    double x1,x2,x3;

    while (fscanf(f,"%lf %lf %lf",&x1,&x2,&x3)==3){
        nl++;
    }
    return nl;
}



double **read_file(char s[],double **arr, int n){

    FILE *f;
    double x1,x2,x3;

    if ((f=fopen(s, "r")) == NULL){
        printf("The file %s cannot be opened for reading.\n",s);
    }

    for (int i=0; i<n; i++){
        fscanf(f,"%lf %lf %lf",&x1,&x2,&x3);
        arr[i][0] = x1;
        arr[i][1] = x2;
        arr[i][2] = x3;
    }

    if (fclose(f) != 0){
        printf("The file %s could not be closed.\n",s);
    }
    return arr;

}

void write_data(char s[], double **arr, int n){

    FILE *f;
    FILE *o;
    if ((f=fopen(s, "r")) == NULL){
        printf("The file %s cannot be opened for reading.\n",s);
    }

    if ((o=fopen("data_out.txt", "w")) == NULL){
        printf("The file data_out.txt cannot be opened for writing.\n");
    }

    double x1,x2,x3;
    for (int i=0; i<n; i++){
        fscanf(f,"%lf %lf %lf",&x1,&x2,&x3);
        fprintf(o,"%.1lf %.1lf %.1lf\n",x1,x2,x3);
    }

}

double *rotate_vector(double vec[3], double a){
    a = a * 3.141 / 180.0;
    //double R[3][3];
    double R[3][3] = {{cos(a), -sin(a) ,0}, {sin(a), cos(a), 0},{0, 0, 1}};
    double *rotated;
    rotated = (double *)malloc(sizeof(double)*3);
    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            rotated[i] += vec[i]*R[j][i];
        }
    }
    return rotated;
}


int main(){
     
    char filename[] = "datain.txt";
    int n = number_of_lines(filename);
    printf("The file has %d lines.\n",n);

    double **arr;

    arr = (double **)malloc(sizeof(double *)*n);
    for (int i=0; i<n; i++){
        arr[i] = (double *)malloc(sizeof(double)*3);
    }
    

    arr = read_file(filename, arr, n);

    for (int i=0; i<n; i++){
        printf("%.1lf %.1lf %.1lf\n", arr[i][0], arr[i][1], arr[i][2]);
    }

    write_data(filename,arr,n);

    double v[3] = {1.0, 1.5, 1.0};

    double *rotated;

    rotated = rotate_vector(v,60);

    printf("%f %f %f\n",rotated[0], rotated[1], rotated[2]);

    // free((void **) arr);
    // for (int i=0; i<n; i++){
    //     free((void *) arr[i]);
    // }

    return 0;
}


