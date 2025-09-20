#include <stdio.h>

//Will Work on Both Terminal and Prutor


int main(void) {
    int N;
    if (scanf("%d", &N) != 1) return 0;


    int freq[101] = {0};

    for (int i = 0, x; i < N; ++i) {
        if (scanf("%d", &x) != 1) return 0;
        if (x >= 1 && x <= 100) freq[x]++;
    }

  
    int items[101], m = 0;
    for (int v = 1; v <= 100; ++v) if (freq[v] > 0) items[m++] = v;

  

    for (int i = 1; i < m; ++i) {
        int key = items[i];
        int j = i - 1;
        while (j >= 0) {
            int a = items[j];
            int worse = 0;
            if (freq[a] < freq[key]) worse = 1;                 
            else if (freq[a] == freq[key] && a > key) worse = 1; 
            if (!worse) break;
            items[j + 1] = items[j];
            --j;
        }
        items[j + 1] = key;
    }

    int first = 1;
    for (int i = 0; i < m; ++i) {
        int v = items[i];
        for (int k = 0; k < freq[v]; ++k) {
            if (!first) putchar(' ');
            printf("%d", v);
            first = 0;
        }
    }
    putchar('\n');
    return 0;
}

