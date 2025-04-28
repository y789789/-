#include <stdio.h>
 
int main(){
    int category = 2;
    float prize = 299.9;

    switch(category){
/*
如果商品类别是电子产品：
价格小于500元，输出“电子产品价格较低，无优惠”。
价格在500元到1000元之间，输出“电子产品可享受 5%的优惠”。
价格大于1000元，输出”电子产品可享受10%的优惠“。
*/        
        case 1:
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
/*
如果商品类别是服装：
价格小于200元，输出“服装价格较低，无优惠”。
价格在200元到500元之间，输出“服装可享受8% 的优惠”。
价格大于500元，输出“服装可享受 15% 的优惠”。
*/            
        case 2:
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

    }
}