//CODE BY BHAVESH G

#include <stdio.h>
#include <math.h>


int main(){
printf("Enter Value of a:");
float a;
scanf(" %f", &a);

FILE *x;
x = fopen("x.dat","w");
for(int i=0; i<1000; i++){
	float x_c = 2*a*i;
fprintf(x,"%.2f, ", x_c);
}
fclose(x);

FILE *y;
y = fopen("y.dat", "w");
for(int j=0; j<1000; j++){
float y_c = a*j*j;
fprintf(y, "%.2f, ", y_c);
}
fclose(y);

return 0;
}




