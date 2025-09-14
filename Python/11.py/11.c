#include <stdio.h>

int n1, n2, n3;

int sum1(int k);

int sum1(int k){
if(k>0 && k<=n1){
return n1*k + sum1(k-1);
}


else return 0;
}


int sum2(int k);

int sum2(int k){
if(k>0 && k<=n2){
return n2*k + sum2(k-1);
}


else return 0;
}


int sum3(int k);

int sum3(int k){
if(k>0 && k<=n3){
return n3*k + sum3(k-1);
}

else return 0;
}



int main(){
printf("Enter 3 Integers:");
scanf(" %d %d %d", &n1, &n2, &n3);

int r1 = sum1(n1);
int r2 = sum2(n2);
int r3 = sum3(n3);

FILE *sums;
sums = fopen("Sum.txt", "w");

fprintf(sums,"%d,%d,%d", r1, r2, r3);

fclose(sums);

if(sums != NULL){
printf("Sum.txt Generated Successfully.\n");
}

else if(sums == NULL){
printf("Sum.txt could not be generated.\n");
}
return 0;
}
