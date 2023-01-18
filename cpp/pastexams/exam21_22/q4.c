#include<stdio.h>
#include<stdlib.h>
#include<math.h>


typedef struct{
    char *filename;
    int num_points;
    double *x;
    double *y;
}data;

typedef struct {
    double k;
    double q;
    double r2;
}fitcoef;

int data_size(char *filename);
int data_read(data *dp);
void print_data(data *dp);
fitcoef linear_fit(data *dp);


int data_size( char *filename){
    FILE *f;
    double x, y;

    int num_cols = 2;
    int counter =0;

    if ((f = fopen(filename,"r"))==NULL){
        printf("Cannot open %s for reading",filename);
        return -1;
    }
    while (num_cols == 2){
        num_cols = fscanf(f,"%1f %1f.\n",&x,&y);
        counter+=1;
    }
    if (fclose(f) != 0){
        printf("File could not be closed.\n");
        return -1;
    }

    return counter - 1;

}

int data_read(data *dp)
{
    FILE *f;

    double x, y;
    int i, N;

    N = dp->num_points;

    if ((f=fopen(dp->filename, "r"))==NULL) {
        printf("Cannot open %s for reading", dp->filename);
        return -1;
    }

    for(i=0; i<N; i++ ) {
        fscanf(f, "%lf %lf", &x, &y);
        dp->x[i] = x;
        dp->y[i] = y;
    }

    if(fclose(f) != 0) {
        printf("File could not be closed.\n");
        return -1;
    }

    return 0;
}

fitcoef linear_fit(data *dp)
{
    /*
    Theory source:
    https://mathworld.wolfram.com/LeastSquaresFitting.html
    */

    fitcoef fc;

    int i;
    double x_mean, y_mean;    
    double ssxx, ssyy, ssxy;

    x_mean = y_mean = 0.0;
    ssxx = ssyy = ssxy = 0.0;

    for(i=0; i<dp->num_points; i++)
    {
        x_mean += dp->x[i];
        y_mean += dp->y[i];
    }
    x_mean /= dp->num_points;
    y_mean /= dp->num_points;

    for(i=0; i<dp->num_points; i++)
    {
        ssxx += (dp->x[i] - x_mean)*(dp->x[i] - x_mean);
        ssyy += (dp->y[i] - y_mean)*(dp->y[i] - y_mean);
        ssxy += (dp->x[i] - x_mean)*(dp->y[i] - y_mean);
    }

    fc.k = ssxy/ssxx;
    fc.q = y_mean - fc.k*x_mean;
    fc.r2 = ssxy * ssxy / ssxx / ssyy;
    
    return fc;
}

void print_data(data *dp)
{
    /*
    Print the content of structure data dp.
    */

    int i;

    printf("\nData file: %s\n", dp->filename);
    printf("Number of data points: %d\n\n", dp->num_points);
    printf("Data points (x_i, y_i):\n");

    for(i=0; i<dp->num_points; i++){
        printf("i=%d:\t (%4.2lf, %4.2lf)\n", i, dp->x[i], dp->y[i]);
    }
}

/* ------------------------------------------------- */
int main(){
    data points;
    fitcoef fc;

    points.filename = "numbers.txt";
    points.num_points = data_size(points.filename);

    points.x = (double *)malloc(sizeof(double)*points.num_points);
    points.y = (double *)malloc(sizeof(double)*points.num_points);

    data_read(&points);
    print_data(&points);

    printf("\nFitting lines y = kx +q to the data...\n");
    fc = linear_fit(&points);

    printf("\nFit coeficients:\n");
    printf("k = %lf\n", fc.k);
    printf("q = %lf\n", fc.q);

    printf("\nCorrelation coefficient:\n");
    printf("R2 = %lf\n\n", fc.r2);

    free((void *) points.x);
    free((void *) points.y);

    return 0;
}
/* ------------------------------------------------- */