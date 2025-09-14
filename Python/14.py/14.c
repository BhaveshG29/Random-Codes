#include <stdio.h>
int n;

int sum(long long int k);

int sum(long long int k){
if(k>0 && k<=n){
return k + sum(k-1);
}

else if(k>0 && k<=2*n){
return k + sum(k-1);
}

else if(k>0 && k<=3*n){
return k + sum(k-1);
}

else if(k>0 && k<=4*n){
return k + sum(k-1);
}


else return 0;
}

int main(){

printf("Enter a Number:");
scanf(" %d", &n);
int result1, result2, result3, result4;

result1 = sum(n);
result2 = sum(2*n);
result3 = sum(3*n);
result4 = sum(4*n);

//Generated sum.dat file
FILE *sum;

sum = fopen("sum.dat","w");

fprintf(sum,"%d,%d,%d,%d", result1,result2,result3,result4);


fclose(sum);

if(sum != NULL){
printf("sum.dat file is gernerated successfully.\n");
}

else if(sum == NULL){
printf("Some error occurred while generating the file. Please Check the Code.\n");
}

return 0;
}
