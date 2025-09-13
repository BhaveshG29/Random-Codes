#include <stdio.h>
#include <string.h>

int main(void){
    char Name[100];
    printf("Enter Your Full Name:");
    if (fgets(Name, sizeof(Name), stdin)) {
        Name[strcspn(Name, "\n")] = '\0';
        printf("Fuck You %s!\n", Name);
    }
    return 0;
}

