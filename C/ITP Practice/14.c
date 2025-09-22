//CODE BY BHAVESH G

#include <stdio.h>

int main() {
    double c, x;
    int N;
    scanf("%lf %d %lf", &c, &N, &x);
    for (int i = 0; i < N; i++) {
        x = 0.5 * (x + c / x);
    }
    printf("%.10f\n", x);
    return 0;
}

