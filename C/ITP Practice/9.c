#include <stdio.h>
#include <string.h>

#define MAXN 1000005 

int main(void) {
    char N[MAXN];
    int K;

    if (scanf("%s", N) != 1) return 0;
    if (scanf("%d", &K) != 1) return 0;

    int L = (int)strlen(N);
    if (K <= 0 || L == 0) return 0;

    int blocks = (L + K - 1) / K;
    printf("%d\n", blocks);

    
    int first_len = L % K;
    if (first_len == 0) first_len = K;

    int pos = 0; 

    for (int b = 0; b < blocks; ++b) {
        int chunk_len = (b == 0) ? first_len : K;

        
        long long mod = 1;
        for (int i = 0; i < chunk_len; ++i) mod *= 10;

        long long value = 0;
        for (int i = 0; i < chunk_len; ++i) {
            value = value * 10 + (N[pos + i] - '0');
            if (value >= mod) value %= mod; 
        }
        int last_digit = N[pos + chunk_len - 1] - '0';

        long long enc = (value + last_digit) % mod;

     
        char buf[32]; 
        long long tmp = enc;
        char out_digit;
        long long pow10 = 1;
        for (int i = 1; i < chunk_len; ++i) pow10 *= 10;
        for (int i = 0; i < chunk_len; ++i) {
            long long d = tmp / pow10;
            out_digit = (char)('0' + (int)d);
            putchar(out_digit);
            tmp %= pow10;
            if (pow10 > 1) pow10 /= 10;
        }

        pos += chunk_len;
    }

    putchar('\n');
    return 0;
}

