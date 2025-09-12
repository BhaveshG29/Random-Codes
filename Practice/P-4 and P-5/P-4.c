#include <stdio.h>
#include <math.h>
 
float a, r;

float sum(int n);

float sum(int n){
if(a!=0 && r!=1 && r!=0 && n<=10){
return a + sum(n-1);
}

else if(r==1 && n<=10){
return a + sum(n-1);
}

else if( r==0 && a==0) return 0;
}


int main(){
printf("Write the first term and the common difference:");
scanf(" %f %f", &a, &r);

float result = sum(10);


FILE *gpsum;

gpsum = fopen("gpsum.dat", "w");

fprintf(gpsum, "%.2f" , result);

fclose(gpsum);

printf("%.2f", result);

return 0;
}
