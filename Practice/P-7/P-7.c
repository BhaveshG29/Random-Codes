#include <stdio.h>
#include <string.h>

char input[];


int main(){

for(int i=0; i<3; i++){

scanf("%s", &input[i]);

fgets(input, sizeof(input), stdin);
}

FILE *in;

input = fopen("input.txt", "w");

for(int i =0; i<3; i++){
fprintf(in, "%s", in[i]);
}

fclose(in);


in = fopen("input.txt", "r");
if(in != NULL){
int words = sizeof(input)/strlen(input);
printf("Lines:");
printf("Words: %d\n", words);
printf()
}

else if(in == NULL){
printf("File Not Found");
}
fclose(input);

return 0;
}

