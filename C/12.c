#include <stdio.h>



int main(){

for(int row=1;row<=3;row++){

for(int col=1;col<=row;col++){
	printf("*");
}

printf("\n");
}

for(int i=1;i<3;i++){
printf("*");
}

for(int row=4;row>=1;row--){

for(int col=1;col<=row;col++){
	printf("*");
}

printf("\n");
}


return 0;
}
