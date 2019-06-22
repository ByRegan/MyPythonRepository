#coding=utf-8

#输入一个正整数
x = int(input())

# 请在此添加代码，将输入的一个正整数分解质因数
#********** Begin *********#
t = x
i = 2
result = []
while True:
    if t==1:
        break
    if t%i==0:
        result.append(i)
        t = t/i
    else:
        i+=1
#********** End **********#

#输出结果，利用map()函数将结果按照规定字符串格式输出
print(x,'=','*'.join(map(str,result)))


