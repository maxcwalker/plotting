#include <stdio.h>

/* main: copy stdin to stdout */
int main(void) {
  int c;
  c=getchar();
  while (c != EOF) {   /* != means 'not equal' */
      putchar(c);
      c=getchar();
    }
  return 0;
}

