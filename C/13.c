// CODE BY BHAVESH G

#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) {
        return 0;
    }

    int a;
    long long max1 = -3000000000LL; 
    long long max2 = -3000000000LL;

    for (int i = 0; i < n; i++) {
        if (scanf("%d", &a) != 1) return 0;

        if (a > max1) {
            max2 = max1;
            max1 = a;
        } else if (a < max1 && a > max2) {
            max2 = a;
        }
    }

    if (max2 == -3000000000LL) {

        printf("No second largest\n");
    } else {
        printf("%d\n", (int)max2);
    }
    return 0;
}

