from unicodedata import category

from setuptools.package_index import user_agent

print("nh"+"djh")
print('let\'s go')
print ("我是第一行\n我是第二行")
print ("\n")
import math
a=-2
b=-1
c=3
print((-b+ math.sqrt(b**2 - 4*a*c))/(2*a))
print((-b- math.sqrt(b**2 - 4*a*c))/(2*a))

# 对字符串求长度
s= ("Hello World!")
print(len(s))

# 通过索引获取单个字符
print(s[0])
print(s[11])

# 布尔类型
b1=True
b2=False


#空值类型
n=None


# type函数
print(type(s))
print (type(b1))
print (type(n))
print (type(1.5))


# BMI = 体重 / （身高 ** 2）
user_weight = float(input ("请输入您的体重  （单位：kg） ："))
user_height = float(input("请输入您的身高 （单位：m) :"))
user_BMI = user_weight / (user_height) **2
print ("您的BMI值为：" + str (user_BMI) )
# 偏瘦：user_BMI <= 18.5
# 正常：18.5 < user_BMI <=25
# 偏胖：25 < user_BMI <=30
# 肥胖：user_BMI >30
if user_BMI <=18.5:
    print("此BMI值属于偏瘦范围")
elif 18.5 < user_BMI <= 25:
    print("此BMI值属于正常范围。")
elif  25 < user_BMI <=30:
    print("此BMI值属于偏胖范围。")
else:
    print("此BMI值属于肥胖范围。")

















mood_index = int (input ("对象今天的心情指数是："))
if mood_index >= 68:
    print("恭喜，今晚应该可以玩游戏，去吧皮卡丘！")
else:   # mood_index < 68
    print("为了自个儿小命，还是别打了。")



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
    user_input  = input('请输入数字(完所有数字输入后，请输入q终止程序'):
 if count == 0:
     result = 0
 else:
     result = total / count
  print("请输入您的数字平均值为" + str(result))


def  calculate_BMI(weight, height):
    BMI = weight / height ** 2
    if BMI <= 18.5
        category = "偏瘦"
    elif BMI <=25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"您的BMI分类为：{category}")
    return BMI














