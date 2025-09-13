#include <stdio.h>
#include <math.h>

long int n;
float a, r;
double gp;

int sum(int k){
if(n<=99999 && r>=1 && r<=-1){

for(k=0; k<n; k++){
if(k<n && a!=0 && r!=0){
	float power = pow(r, k);
gp = gp + a*power; 
	continue;
}

else if(k>=n && k<0 && a==0 && r==0){return 0;}
}

}

else if(n>99999  && r<=1 && r>=-1){
if(r !=1){
gp = a/(1-r);
}

else if(r==1){
	gp = n*a;

}

}
}


int main(){
printf("Enter the First Term and Common Ration:");
scanf(" %f %f", &a, &r);

printf("Enter the number of terms:");
scanf(" %ld", &n);
sum(n-1);
double result = gp;

FILE *GPSUM;
GPSUM = fopen("GPSUM.tex","w");
if(n<=99999){
fprintf(GPSUM, "The Sum of %ld terms of Geometric Progression with First term as %.2f and Common Ratio %.2f is %.2lf.\n", n, a, r, result);
printf("Saved GPSUM.tex file.\n");
}

else if(n>99999){
fprintf(GPSUM, "The Sum of Infinite Geometric Progession with First term as %.2f and Common Ratio %.2f is %.2lf.\n", a, r, result);
printf("Saved GPSUM.tex file.\n");
}

fclose(GPSUM);

return 0;
}
