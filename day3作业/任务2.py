max = 0
sum = 0
for i in range(10):
    our = int(input('请输入数字：'))
    if our > max:
        max = our
    sum = sum + our
print("最大值为：", max)
print("总和为:",sum)
print("平均数为：", (sum / 10))