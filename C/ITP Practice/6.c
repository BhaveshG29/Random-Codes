//CODE BY BHAVESH G

#include <stdio.h>

int main(void) {
    int n, k;
    scanf("%d %d", &n, &k);

    int a[n];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    if (n > 0) {
        k %= n;                  
      
        for (int l = 0, r = n - 1; l < r; l++, r--) {
            int t = a[l]; a[l] = a[r]; a[r] = t;
        }
        
        for (int l = 0, r = k - 1; l < r; l++, r--) {
            int t = a[l]; a[l] = a[r]; a[r] = t;
        }
        
        for (int l = k, r = n - 1; l < r; l++, r--) {
            int t = a[l]; a[l] = a[r]; a[r] = t;
        }
    }

    for (int i = 0; i < n; i++) {
        if (i) printf(" ");
        printf("%d", a[i]);
    }
    printf("\n");
    return 0;
}

