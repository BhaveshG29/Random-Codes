#include <stdio.h>
#include <math.h>


int main(){

int A[2]={2,1};
int B[2]={0,5};
int C[2]={-1,2};


float m1 = fabs((A[1] - B[1])/(A[0] - B[0]));
float m2 =fabs((C[1] - B[1])/(C[0] - B[0]));
 
if(m1 == m2){
printf("The Points A, B, C are collinear.\n");
}

else if(m1 != m2){

printf("The Points A, B, C are not collinear.\n");
}

printf("Since, m1=%.2f and m2=%.2f\n", m1, m2);

return 0;
}
