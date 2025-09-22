//CODE BY BHAVESH G

#include <stdio.h>
#include <string.h>

int main() {
    char a[500], b[500];
    int cnt[256] = {0};
    
    scanf("%499s %499s", a, b);

    if (strlen(a) != strlen(b)) {
        printf("no\n");
        return 0;
    }

    for (int i = 0; a[i]; i++) {
        cnt[(unsigned char)a[i]]++;
        cnt[(unsigned char)b[i]]--;
    }

    for (int i = 0; i < 256; i++) {
        if (cnt[i]) {
            printf("no\n");
            return 0;
        }
    }
    

    printf("yes\n");

    return 0;
}

