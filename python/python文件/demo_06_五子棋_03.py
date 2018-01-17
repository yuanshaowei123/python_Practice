'''
    五子棋第3个版本
        在第2个版本基础上判断输赢
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

    #判断输赢
    #1 行上形成5子连珠
    for i in range(size):
        rowStr= ""
        for j in range(size):
            rowStr += arr[i][j]

        if(rowStr.__contains__("赢赢赢赢赢")):
            print("行上形成了五子连珠 ， 恭喜您战胜了电脑!")
            exit()

    #2 列上形成5子连珠
    for i in range(size):
        colStr= ""
        for j in range(size):
            colStr += arr[j][i]

        if(colStr.__contains__("赢赢赢赢赢")):
            print("列上形成了五子连珠 , 恭喜您战胜了电脑!")
            exit()
    #3 正对角线形成5子连珠
    #3.1 左下角
    for i in range(size):
        row = i
        col = 0

        while row <= size-1:

            leftDownStr = ""
            while row <= size-1:
                leftDownStr += arr[row][col]

                row = row +1
                col = col +1

            #print(leftDownStr)

            if(leftDownStr.__contains__("赢赢赢赢赢")):
                print("左下方形成了五子连珠 , 恭喜您战胜了电脑!")
                exit()

   # while True:




    #4 反对角线形成5子连珠