#include <stdio.h>

int main(){
    int year = 2088;

    if (((year % 4 == 0) && !(year % 100 == 0)) || (year % 400 == 0)){
        printf("%d年是闰年\n",year);
    }
    else {
        printf("%d年不是闰年\n",year);
    }
}