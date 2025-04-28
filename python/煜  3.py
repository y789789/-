shopping_list = []
shopping_list .append("键盘")
shopping_list .append("键帽")
shopping_list .remove("键帽")
shopping_list.append("音响")
shopping_list .append("电竞椅")
shopping_list [1]= "硬盘"

# print(shopping_list )
# print(len(shopping_list) )
# print(shopping_list [0])

price = [799, 1024, 200, 800]
max_price = max(price)
min_price = sorted(price)
print(max_price)
print(min_price)
print(sorted_price)


print("哈喽呀，我是一个求平均值的程序。")
total = 0
count = 0
user_input= input("请输入数字(完成所有数字输入后，请输入q终止程序)：")
while user_input !="q":
    num = float(user_input )
    total += num
    count += 1
    user_input  = input("请输入数字(完成所有数字输入后，请输入q终止程序)：")
 if count == 0:
     result = 0
 else:
     result = total / count
  print("请输入您的数字平均值为" + str(result))
