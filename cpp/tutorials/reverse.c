#include<stdio.h>

long string_length(char s[]){
	int nc=0;
	int i=0;
	while (s[i] != '\0'){
		nc++;
	}
	return nc;
}

char reverse(char in[], char out[]){
	int sl = string_length(in)-1; // good to know the length
	int i=0;
	while (in[i] != '\0'){
		out[sl-i] = in[i];
	}
	out[sl] = '\0';
	return out[];
}

int main(void) {
	char s1[]="Hello";
	char s2[]="x";
	char s3[]="line 1\tline 2\n";
	
	printf("%20s | %s\n", "string_length(s)", "s");
	printf("%20ld | %s\n", string_length(s1), s1); 
	printf("%20ld | %s\n", string_length(s2), s2);
	printf("%20ld | %s\n", string_length(s3), s3); 
	return 0;
}
