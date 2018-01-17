'''
    五子棋第2个版本
        在第1个版本基础上加入用户下棋和电脑随机下棋
        并且需要处理下棋时候落子位置已经有棋的情况
'''
import random   #导入随机数模块

size = int(input("请输入五子棋棋盘大小size:\n"))  # 自定义棋盘大小并转换为int型

arr = []
#初始化棋盘方法
def initMap(arr):
    for i in range(size):
        arr.append([])
        for j in range(size):
            arr[i].append("口")

#打印棋盘方法
def printMap(arr):
    size = len(arr)
    for i in range(size):
        for j in range(size):
            print(arr[i][j] , end=" ")
        print()

initMap(arr)
printMap(arr)

while True:

    while True:
        #我方下棋
        value = input("请输入下棋的坐标,格式如下: 1,2\n")
        values = value.split(",")

        if arr[int(values[0])][int(values[1])] == "口":
            arr[int(values[0])][int(values[1])] = "赢"
            break
        else:
            print("此处有棋子 ， 落子失败!")
            continue

    while True:
        #电脑下棋
        intX = random.randint(0 , size-1)
        intY = random.randint(0 , size-1)

        if arr[intX][intY] == "口":
            arr[intX][intY] = "输"
            break
        else:
            continue

    printMap(arr)