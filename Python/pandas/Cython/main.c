#include <stdio.h>


int main(){
float m;

printf("Enter the Value of 'm' for Line y = mx:");
scanf("%f", &m);


FILE *cords;

cords = fopen("cords.csv", "w");
fprintf(cords,"x,y\n");

for(float i =-100; i<=100; i+=0.01){
fprintf(cords, "%.2f,%.2f\n", i, m*i);
}

fclose(cords);

return 0;
}
