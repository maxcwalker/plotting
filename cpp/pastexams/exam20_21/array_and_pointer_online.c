/*************************************
 This function explores differences between array and pointer declarations.
 
 The program includes the data types of different experssions.  These were obtained by
 using "gcc -Wall" to compile the code.  This will show all warnings, including the 
 data type of arguments in printf does not match what is indicated in the format string.
 
 Findings:
  1. In a formal argument to a function, using pointer or array has no difference; it is
	always treated as a pointer.  This makes sense, since the argument expects an address,
	and really does not know anything else about the address.
	
  2. Main difference.  One can assign to a pointer variable, but not an array variable.  
     That is, given:
		int b[3]; 
		int *a, *c;
		a = c;  		// has meaning and can compile,
		b = c;			// has no meaning, and cannot compile.
				// Error is "assignment to expression with array type"
				// This makes sense since b's address is set at compile time
	Similarly,
		*(&a) = c;     // is okay
		*(&b) = c'     // does not compile;
		
  3. When a variable is declared as array, e.g., int b[3];  Then &b will results in the 
    same value as b; however, &b has a different data type: b is of type int[3], and 
	&b is of type int (*)[3].  

  4. Using & on an array datatype seems to have no legitimate reason. 
 ************************************/


#include <stdio.h>

void func1 (int a[2]) {
    int b[3] = {2, 2, 2};

    printf("Func 1: Datatypes: a is int[], b is int[] \n");
	printf("Type of a is (int *);     value is %d\n", a);		   // a is (int *)
	printf("Type of &a is (int **);   value is %d\n", &a);		   // &a is (int **)
	printf("Type of &a[0] is (int *); value is %d\n", &a[0]);   // &a[0] is (int *)
	
	printf("Type of b is (int *);     value is %d\n", b);           // b is (int *)
	printf("Type of &b is int (*)[3]; value is %d\n", &b);		   // &b is int (*)[3]
	printf("Type of &b[0] is (int *); value is %d\n", &b[0]); // &b[0] is (int *)
	
	printf("The code \"*(&b) = a;\" or \"b=a\" won't compile. Error: assignment to expression with array type \n\n");
	// There is no point using (&b) on an array
	// *(&b) = a;
	//b = a;
}

void func2 (int *a) {
    int *b = (int *) malloc(sizeof(int) * 3);
	b[0] = 2;  b[1] = 2;  b[2] = 2;
	
    printf("Func 2: Datatypes: a is int*, b is int*\n");
	printf("Type of a is (int *);     value is %d\n", a);		   // a is (int *)
	printf("Type of &a is (int **);   value is %d\n", &a);		   // &a is (int **)
	printf("Type of &a[0] is (int *); value is %d\n", &a[0]);   // &a[0] is (int *)
	
	printf("Type of b (int *);        value is %d\n", b);           // b is (int *)
	printf("Type of &b is (int **);   value is %d\n", &b);		   // &b is int (*)[3]
	printf("Type of &b[0] is (int *); value is %d\n", &b[0]); // &b[0] is (int *)
	
	printf("The code \"*(&b) = a;\" will compile \n\n");
	*(&b) = a;
	a=b;
}

int main() {
  //int data1[3] = {1, 1, 1};
  int *data2 = (int *) malloc(sizeof(int) * 3);
  data2[0] = 1;  data2[1] = 1;  data2[2] = 1;
 
  //printf("Using int[] to call the functions\n\n");
  //func1(data1);
  //func2(data1);
  
  printf("Using int* to call the functions\n\n");
  func1(data2);
  func2(data2);
  return 0; 
}