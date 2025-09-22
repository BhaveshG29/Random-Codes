//CODE  BY BHAVESH G

#include <stdio.h>

int main() {
    unsigned long long R;
    scanf("%llu", &R);

    unsigned long long need = 0;
    unsigned long long grains = 1;
    
    for (int i = 0; i < 49; i++) {
        need += grains;
        grains *= 2;
    }

    if (R >= need) {
        
        printf("YES\n%llu\n", R - need);
    } 

    else {
        
        unsigned long long sum = 0;
        grains = 1;
        int filled = 0;
        
	while (filled < 49 && sum + grains <= R) {
            sum += grains;
            grains *= 2;
            filled++;
        }
        
	printf("NO\n%d\n", filled);
    }

    return 0;
}


