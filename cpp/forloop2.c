#include<stdio.h> 
#include<math.h>      /* include math-header for sqrt-function */

int main( void ) {
  /* print table of N square roots sqrt(x) for x in [a,b] */

  int N = 19;         /* total number of lines in table */
  double a=1;         /* starting with x=a */
  double b=10;        /* ending with x = b */
  double x;           /* being used in for-loop */
  int i;              /* iteration counter for for-loop */

  for (i=0; i<N; i++) {
    x = a + i*(b-a)/(N-1);  /* compute x */

    /* compute sqrt(x) and print result */
    printf(" sqrt(%f) = %f\n", x, sqrt(x) );
  }

  return 0;
}
