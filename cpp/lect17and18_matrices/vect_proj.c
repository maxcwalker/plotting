#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int read_number_lines(char s[]){

    FILE *fr;
    double x1, x2, x3;
    int n;

    if ((fr=fopen(s,"r"))== NULL){
        printf("Cannot open the file data.txt.\n");
        return -1;
    }

    n=0;
    while ((fscanf(fr,"%1f %1f %1f", &x1, &x2, &x3)) == 3){
        n+=1;
    }

    if (fclose(fr)==EOF){
        printf("File could not be closed.\n");
        return -1;
    }

    return n;
}


int read_data(char s[], double **m, int n){

    FILE *fr;
    int i;

    if ((fr=fopen(s,"r"))==NULL){
        printf("Cannot open the file %s.\n",s);
        return -1;
    }

    for (i=0; i<n; i++){
        fscanf(fr,"%1f %1f %1f", &m[i][0], &m[i][1], &m[i][2]);
    }

    if (fclose(fr) == EOF){
        printf("File %s could not be closed.\n",s);
        return -1;
    }

    return 0;
}


int write_data(char s[], double **m, int n){

    FILE *fw;
    int i;

    if ((fw=fopen(s,"w"))==NULL){
        printf("Cannot open the file %s.\n",s);
        return -1;
    }

    for (i=0; i<n; i++){
        fprintf(fw,"%1f %1f %1f\n", m[i][0], m[i][1], m[i][2]);
    }

    if (fclose(fw) == EOF){
        printf("File %s could not be closed.\n",s);
        return -1;
    }

    return 0; //function returns 0 if successfull
}


void project_vector(double v[], double wref[]){
    double wref_norm; 
    double dot_prod; 
    int i;

    /* normalise reference vector wref to a unit vector */
    wref_norm = sqrt(wref[0]*wref[0] + 
                     wref[1]*wref[1] + 
                     wref[2]*wref[2]);

    for (i=0; i<3; i++){ 
        wref[i] /= wref_norm;
    }

    /* calculate the dot product of the input vector v
       and the normalised reference vector wref */

    dot_prod = 0.0; 
    for(i=0; i<3; i++) {
    dot_prod += v[i]*wref[i]; 
    }

    /* evaluate the vector projection */
    for(i=0; i<3; i++) {
    v[i] = dot_prod*wref[i];
    }
}


int main(){

    FILE *fr,*fw;
    int i,j,n;
    double **m;
    double v[3];
    double wref[3] = {1.0, 0.0, 0.0}; // reference vector

    char s_in[] = "data.txt";
    char s_out[] = "data_out.txt";

    n = read_number_lines(s_in);

    m = (double **)malloc(n*sizeof(double *));

    if (m == NULL){
        printf("error: out of memory.\n");
        return 1;
    }


    for (i=0; i<n; i++){
        m[i] = (double *)malloc(3*sizeof(double));
        if (m[i] == NULL){
            printf("error: out of memory.\n");
            return 1;
        }
    }

    read_data(s_in, m, n);

    for (i=0; i<n; i++){

        for (j=0; j<3; j++){
            v[j] = m[i][j];
        }

        project_vector(v, wref);

        for (j=0; j<3; j++){
            m[i][j] = v[j];
        }
    }

    write_data(s_out, m, n);

    return 0;
}
