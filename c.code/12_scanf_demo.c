#include <stdio.h>
 
int main(){
    char category;
    float prize;
      
    printf("商品类别有A_电子产品， B_服装\n请按顺序输入商品类型和价格， 两个值中间用空格隔开：");
    scanf(" %c %f", &category, &prize);

    switch(category){
        case 'A':
            if (prize < 500){
                printf("电子产品价格较低，无优惠");
            }
            else if(prize <= 1000){
                printf("电子产品可享受5%%的优惠\n");
            }
            else{
                printf("电子产品可享受10%%的优惠\n");
            }
            break;

        case 'B':
            if (prize < 200){
                printf("服装价格较低，无优惠\n");
            }
            else if (prize <=500){
                printf("服装可享受8%%的优惠\n");
            }
            else {
                printf("服装可享受 15%%的优惠\n");
            }
            break;
        default:
            printf("找不到该商品类别\n");
            break;    

    }
}

