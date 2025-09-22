//CODE BY BHAVESH G

#include <stdio.h>
#include <math.h>



int main(){
int n;
int temp,dc;
scanf("%d", &n);

if(n>9){
	dc=0;
for(temp=n; temp>=1;){
	temp = temp/10;
	dc++;
}

temp = n;
long int sum = 0;
int p=1;
while(temp>0){
int d = temp % 10;
int p = pow(d,dc);

sum += p;
temp = temp/10;
}

if(sum==n){
printf("TRUE\n");
}

else{
printf("FALSE\n");}
}




else if(n<=9 && n>=0){
dc = 1;
printf("TRUE\n");
}


return 0;
}
