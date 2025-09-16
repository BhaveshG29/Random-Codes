#include <stdio.h>
#include <math.h>


int main(){

double x;
int k;
double l=0;
double pow1;
int pow2;

scanf("%lf %d", &x, &k);

for(int i=1; i<=k;i++){
pow1 = pow(x,i);
pow2 = pow(-1, i+1);
l += (pow1*pow2)/i;
}

printf("%.4lf\n", l);


return 0;
}
