
'''
    第1个版本：先准备好一个n*n的二维列表 并打印到控制台

    数独游戏的规则（输入一个大于1的奇数）
    a  1放到第一行的中间
    b 下一个数字放到上一个数字的右上角，如果超出范围了
        行和列超出了之后往回折 折到底
    c 如果数字是奇数的倍数，下一个数字直接放该数字的下边
        而不用考虑b
'''

print('请输入一个奇数开始游戏或者exit退出')
content = input("请输入:")

# 转换输入值为整型
length = int(content)

# 定义空列表用来存储行和列及对应数值
arr = []
for i in range(length):
    arr.append([])  # 追加行
    for j in range(length):
        arr[i].append("口")  # 追加列

# 打印二维列表arr

for i in range(length):
    for j in range(length):
            print(arr[i][j] , end=" ")
    print("")

#print(arr)
    