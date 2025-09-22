//CODE BY BHAVESH G

#include <stdio.h>
#include <string.h>

int main() {
    char n[100];
    int k;
    scanf("%s %d", n, &k);
    
    int len = strlen(n);
    int count = 0;
     
    if (strcmp(n, "00") == 0 && k == 0) {
        printf("0\n");
        return 0;
    }
    
    for (int i = 0; i < len; i++) {
        int digit_sum = 0;
        for (int j = i; j < len; j++) {
            digit_sum += (n[j] - '0');
            if (digit_sum <= k) {
                count++;
            } else {
                break;
            }
        }
    }
    
    printf("%d\n", count);
    return 0;
}

