//CODE BY BHAVESH G

#include <stdio.h>

void printRhombus(int n) {

    for (int i = 1; i <= n; ++i) {
        for (int s = 0; s < n - i; ++s){ 
		printf(" ");
	}

        for (int x = i; x >= 2; --x){ 
		printf("%d", x);
	}
        
	for (int x = 1; x <= i; ++x){ 
		printf("%d", x);
	}
        printf("\n");
    }
    
    for (int i = n - 1; i >= 1; --i) {
        for (int s = 0; s < n - i; ++s) {
		printf(" ");
	}

        for (int x = i; x >= 2; --x){ 
		printf("%d", x);
	}

        for (int x = 1; x <= i; ++x){ 
		printf("%d", x);
	}

        printf("\n");
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    
    printRhombus(n);
    
    return 0;
}



