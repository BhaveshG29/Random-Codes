//CODE BY BHAVESH G

#include <stdio.h>

int main() {
    int N;
    if (scanf("%d", &N) != 1) {
        return 1;
    }

    int present[N+1];
    for (int i = 1; i <= N; i++) {
        present[i] = 0;
    }

    for (int i = 0; i < N - 2; i++) {
        int x;
        scanf("%d", &x);
        if (x >= 1 && x <= N) {
            present[x] = 1;
        }
    }

    int missing1 = 0, missing2 = 0;
    for (int i = 1; i <= N; i++) {
        if (present[i] == 0) {
            if (missing1 == 0) {
                missing1 = i;
            } else {
                missing2 = i;
                break;
            }
        }
    }

    if (missing1 < missing2) {
        printf("%d %d\n", missing1, missing2);
    } else {
        printf("%d %d\n", missing2, missing1);
    }

    return 0;
}

