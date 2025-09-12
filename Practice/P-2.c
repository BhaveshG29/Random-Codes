#include <stdio.h>

int main(){
FILE *a;
a = fopen("a.tex", "w");

fprintf(a, "Hello World!");
fprintf(a, "\nHi");
fclose(a);
return 0;
}
