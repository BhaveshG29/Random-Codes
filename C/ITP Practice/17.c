#include <stdio.h>

//Will Show Error in Terminal But Gives Correct Output on Prutor

int main(){
    int r,c;
    scanf("%d %d", &r, &c);
    
    int A[r][c];
    int B[r][c];
    
    for(int i=0; i<r;i++){
        for(int j =0; j<c;j++){
        scanf("%d ", &A[i][j]);
        }
        scanf("");
    }
    
    for(int i=0; i<r;i++){
        for(int j =0; j<c;j++){
        scanf("%d ", &B[i][j]);
        }
        scanf("");
    }
    int sum=0;
    int p=1;
    for(int i=0;i<r;i++){
        for(int j=0; j<c;j++){
        p = A[i][j]*B[i][j];
        
        sum +=p;
            
        }
        
    }
    
    printf("%d", sum);
    return 0;
    
}
