//CODE BY BHAVESH G

#include <stdio.h>

int main(){
    int age;
    scanf("%d", &age);
    
    if(age<=2){
        printf("0");
    }
    
    else if(age>2 && age<=12){
        
        printf("490");
    }
    
    else if(age>=65){
        printf("510");
        
    }
    
    else{
        printf("1000");
    }
    
    return 0;
}
