#include <stdio.h>

int main(){
FILE *a;

a= fopen("a.tex", "a");

fprintf(a, "\nHi, I came from P-3.c");
fclose(a);

return 0;
}
