from setuptools.windows_support import hide_file

with open("./poem.txt", "w",encoding="utf-8")as f:
    f.write("我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒。 \n")


with open("./poem.text", "a", encoding= "utf-8")as f:
    f.write("起舞弄清影, \n")
    f.write("何似在人间。")



a = """我家大门常打开
欢迎你们到来
赶紧"""
print(a)

a = input('请输入第一个数字：')
b = input("请输入第二个数字：")
print(a + b)








