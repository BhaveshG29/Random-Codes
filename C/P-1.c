#include <stdio.h>


int main(){
int a, b;
scanf("%d %d", &a, &b);
if(a>=b){
printf("Remainder of %d/%d = %d\n", a, b, a%b);
}

else if(b>=a){
printf("Remainder of %d/%d = %d\n", b, a, b%a);
}

else if(a==0 || b==0){
for(int i=0; i<=5; i++)	{printf("Error!!\n");
}
}
return 0;
}
