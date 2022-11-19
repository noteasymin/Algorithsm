#include <stdio.h>

int main(void){
    int i;
    double num, result;

    for(i = 0; i < 12; i ++){
        scanf("%lf", &num);
        result = result+num;
    }
    result = result/12;
    printf("%.2f\n", result);

    return 0;
}