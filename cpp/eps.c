#include<stdio.h>
int main(void) {
  double eps = 1.0;
  while (1.0+eps>1.0) {
    eps /= 2.0;
  }
  printf("eps is approximately %g.\n", eps);
  return 0;
}
