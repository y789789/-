#include <stdio.h>
 
int main(){
    char ch = 'A';
    char* ptr = &ch;

    printf("%c\n",*ptr);
    *ptr = 'a';
    printf("%c\n",*ptr);
}