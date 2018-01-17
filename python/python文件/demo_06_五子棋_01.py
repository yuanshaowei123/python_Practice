'''
    五子棋第1个版本
        定义绘制棋盘函数
        定义打印棋盘函数
'''

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