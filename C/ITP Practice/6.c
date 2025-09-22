//CODE BY BHAVESH G

#include <stdio.h>

int main(void) {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;

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
        if (i) putchar(' ');
        printf("%d", a[i]);
    }
    putchar('\n');
    return 0;
}

