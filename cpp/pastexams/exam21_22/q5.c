#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define N 2 //length of vector

double vector_norm(double *v){
    return sqrt(v[0]*v[0] + v[1]*v[1]);
}

void unit_vector(double *v){
    double norm = vector_norm(v);
    v[0] /= norm;
    v[1] /= norm;
}

void rotation_matrix(double **R, double theta){// the ** is because its 2x2
    R[0][0] = cos(theta);
    R[0][1] = -sin(theta);
    R[1][0] = sin(theta);
    R[1][1] = cos(theta);
}  

void rotate_vector(double **R, double *v){
    int i, j;
    double w[2] = {0.0, 0.0};

    for (i=0;i<N; i++){
        for (j=0; j<N; j++){
            w[i] += R[i][j]*v[j];
        }
    }
    // to return it through the input argument v
    for (i=0; i<N; i++){
    v[i] = w[i];
    }
}

double rotation_sequence(double *v, double theta, int n){
    double v0[2], dv[2];
    double **R;

    int i;
    double dtheta = theta / n;
    double vnorm_sum = 0.0;

    R = (double **)malloc(sizeof(double *)*2);
    R[0] = (double *)malloc(2*sizeof(double));
    R[1] = (double *)malloc(2*sizeof(double));

    for (i=1; i<n; i++){
        //printf("%lf\n", theta_min + dtheta*i);

        v0[0] = v[0];
        v0[1] = v[1];

        //theta = theta_min + dtheta*i;
        rotation_matrix(R, dtheta);
        rotate_vector(R,v);

        dv[0] = v[0] - v0[0];
        dv[1] = v[1] - v0[1];

        vnorm_sum += vector_norm(dv);
    }

    free((void *) R[0]);
    free((void *) R[1]);
    free((void **) R);

    return vnorm_sum;
}

double **find_rotation_matrix(double *v, double *w){

    double **R;
    double dotproduct, theta;

    R = (double **)malloc(sizeof(double *)*2);
    R[0] = (double *)malloc(2*sizeof(double));
    R[1] = (double *)malloc(2*sizeof(double));

    unit_vector(v);
    unit_vector(v);
    dotproduct = v[0]*w[0] + v[1]*w[1];

    theta = acos(dotproduct);

    rotation_matrix(R,theta);
    //printf("Print angle: %lf\n", theta*180.0/M_PI);

    return R;
}

//////////////////////////////////////////////
void print_vector(double *v) {
    printf("[%5.3lf, %5.3lf]\n", v[0], v[1]);
}

void print_matrix(double **R) {
    printf("|%5.3lf\t%5.3lf|\n", R[0][0], R[0][1]);
    printf("|%5.3lf\t%5.3lf|\n", R[1][0], R[1][1]);
}

//////////////////////////////////////////////
int main()
{

    double **R;
    double u[N] = {1.0, 0.0};
    double v[N] = {1.0, 1.0};
    double w[N] = {0.0, 1.0};

    double theta = M_PI_2/2.0; // M_PI_2 from math.h

    int num_theta = 100;
    double arc_len;

    R = (double **) malloc(2*sizeof(double *));
    R[0] = (double *) malloc(2*sizeof(double));
    R[1] = (double *) malloc(2*sizeof(double));

    printf("\nVector u:\n");
    print_vector(u);

    printf("\nRotation angle: %lf rad (%5.2lf deg)", theta, theta*180.0/M_PI);

    rotation_matrix(R, theta);
    printf("\nRotation matrix R:\n");
    print_matrix(R);
    rotate_vector(R, u);

    printf("\nVector u rotated by R:\n");
    print_vector(u);

    free((void *) R[0]);
    free((void *) R[1]);
    free((void **) R);

    printf("\nVector v:\n");
    print_vector(v);
    printf("Vector w:\n");
    print_vector(w);

    printf("\nMatrix rotating v to w:\n");
    R = find_rotation_matrix(v, w);
    print_matrix(R);
    printf("\n");

    free((void *) R[0]);
    free((void *) R[1]);
    free((void **) R);

    printf("Rotating vector v: ");
    print_vector(v);
    arc_len = rotation_sequence(v, theta, num_theta);
    printf("by %lf rad (%5.2lf deg)", theta, theta*180.0/M_PI);
    printf(" in %d steps.\n", num_theta);
    printf("Traversed arc length: %lf.\n", arc_len);
    printf("The final vector is: ");
    print_vector(v);
    printf("\n");

    return 0;
}