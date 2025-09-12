#include <stdio.h>
#include <math.h>


struct Structure{

double a, r, d;
int n;
char Type;
};

struct Structure s1;
struct Structure s2;

float AP(int k);

float AP(int k){

if(k<=s1.n && k>0){
	
	return s1.a + (k-1)*s1.d + AP(k-1);

}

else return 0;
}



float GP(int k);

float GP(int k){
if(k<=s2.n && k>0 && s2.a!=0){
float power = pow(s2.r, k-1);

return s2.a*power + GP(k-1);
}

else return 0;
}



int main(){

printf("Enter 'A' for finding sum of n-terms of a AP.\n");
printf("Enter 'G' for finding the sum of n-terms of a GP.\n");
printf("Enter your Preference:");
scanf(" %s", &s1.Type);

if(s1.Type == 'A'){
printf("Enter the First Term and the Comman Difference:");
scanf(" %lf %lf", &s1.a, &s1.d);
printf("Enter the number of terms:");
scanf(" %d", &s1.n);

double result = AP(s1.n);

FILE *sum;

sum = fopen("SUM.tex", "w");

fprintf(sum, "The Sum of %d-terms of an AP with First Term as %.3lf and Common Difference as %.3lf is %.3lf ", s1.n, s1.a, s1.d, result);
printf("Saved SUM.tex file.\n");
	fclose(sum);

}




else if(s1.Type == 'G'){

printf("Enter the First Term and the Comman Ratio:");
scanf(" %lf %lf", &s2.a, &s2.r);
printf("Enter the number of terms:");
scanf(" %d", &s2.n);

double result = GP(s2.n);

FILE *sum;

sum = fopen("SUM.tex", "w");

fprintf(sum, "The Sum of %d-terms of an GP with First Term as %.3lf and Common Ratio as %.3lf is %.3lf ", s2.n, s2.a, s2.r, result);
printf("Saved SUM.tex file.\n");
	fclose(sum);

}

return 0;
}
