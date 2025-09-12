#include <stdio.h>

int main(){

FILE *gpsum;

gpsum = fopen("gpsum.dat", "r");

char sum[123];
fgets(sum, 123, gpsum);

printf("%s", sum);

fclose(gpsum);

return 0;
}
