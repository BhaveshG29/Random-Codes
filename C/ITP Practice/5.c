//CODE BY BHAVESH G

#include <stdio.h>



int main(){
long int N;
long long int sum=0;

scanf("%ld", &N);

long long int P=1;

for(int i=1;i<=N;i++){

P *= i;

sum += P;

}

printf("%lld\n", sum);

return 0;

}
