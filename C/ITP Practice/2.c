//CODE BY BHAVESH G

#include <stdio.h>
#include <math.h>


double sum(float p,int k);


double sum(float p, int k){
if(k>0){
int pow1 = pow(-1,k+1);
double pow2 = pow(p, k);
return (pow1*pow2)/k + sum(p, k-1);
}

else return 0;
}


int main(){
int n;
float x;
scanf("%f %d", &x, &n);

printf("%.4lf\n", sum(x, n));
}
