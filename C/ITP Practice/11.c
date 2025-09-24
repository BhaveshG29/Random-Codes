//CODE BY BHAVESH G

#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool prime(long int n){
    
    if(n<=1){ return false;}
    
    else if(n==2){ return true;}
    
    else if(n%2==0){ return false;}
    
    for(int i=3; i*i<=n; i+=2){
            if(n%i==0){
                return false;
     }
   }
   return true;
}


int large(int p);


int f(int x){
    prime(x);
    if(prime(x) == true){
        return 2*x + 1;
    }
    else if(prime(x) == false){
        return large(x);
    }
}


int g(int y){
    if(y%4<2){
        int result = ((int)pow(y,3) + 11)%3;
        return result;
    }
    
    else if(y%4>=2){
        int result = ((int)pow(y,19) - 8)%5;
        return result;
    }
}



int large(int p){
    int large_prime = -1;
    for(int i=2;i<=p; i++){
if(p%i == 0 && prime(i)==true){
    if(i>large_prime){
    large_prime = i;
}
}
}
    return large_prime;
}


int prime_factorization(long int w, long int prime_factors[20], int expo[20]){
    int count = 0;
    long int temp = w;

    for(long int i = 2; i * i <= temp; i++){
        if(temp % i == 0 && prime(i) == true){
            prime_factors[count] = i;
            expo[count] = 0;
            while(temp % i == 0){
                expo[count]++;
                temp /= i;
            }
            count++;
        }
    }
    if(temp > 1){
        prime_factors[count] = temp;
        expo[count] = 1;
        count++;
    }
    return count;
}


int main(){
   long int N;
   int M;
   scanf("%ld %d", &N, &M);
   
   long int S = 1;
    long int prime_factors[20];
    int expo[20];
    int k = prime_factorization(N, prime_factors, expo);

    for(int i=0; i<k; i++){
        int pi = prime_factors[i];
        int ei = expo[i];
        int fi = f(pi);
        int hi = g(f(ei+1));
        S = S * pow(fi,hi);
    }

   
    printf("%ld\n", S%M);
    return 0;
}
