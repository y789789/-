 #include <stdio.h>

 int main(){
     int user_type == 2;
     double prize = 360; 
     double pay = 0; //

     if (user_type == 1){    //
         if (prize > 100){
            pay = prize * 0.95;
         }
         else{
            pay = prize;
         }
     }
     else if (user_type = 2) {  //
         if (prize > 200){
            pay = prize * 0.9;
         }  else {
            pay = prize; //
         }
     }
     else{
        printf("该用户类型无效\n");
     }
     printf("最终支付金额为：%.2lf\n", pay);  //
 }