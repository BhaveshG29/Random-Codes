// CODE BY BHAVESH G

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    unsigned long long a = 1, b=1;
    for (int i = 2; i <= n; i++) {
        unsigned long long c = a + b;
        a = b;
        b = c;
    }
    printf("%llu\n", b);
    return 0;
}



