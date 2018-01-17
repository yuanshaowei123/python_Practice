
'''
    第3个版本：实现多次进行这个游戏并加入一些容错处理

    数独游戏的规则（输入一个大于1的奇数）
    a  1放到第一行的中间
    b 下一个数字放到上一个数字的右上角，如果超出范围了
        行和列超出了之后往回折 折到底
    c 如果数字是奇数的倍数，下一个数字直接放该数字的下边
        而不用考虑b
'''
#无限循环，直到用户输入exit，可以反复玩游戏
while True:
    print('请输入一个奇数开始游戏或者exit退出')
    content = input("请输入:")
    # 输入exit退出
    if "exit" == content:
        exit()
    # 判断是否为数字，不是则continue跳出当次循环重新输入
    if not content.isdigit():
        print('输入的不是数字')
        continue
    # 转换输入值为整型
    length = int(content)
    # 判断非奇数跳出当次循环重新输入
    if length % 2 == 0 :
        print('输入的数字不是奇数')
        continue
    # 定义空列表用来存储行和列及对应数值
    arr = []
    for i in range(length):
        arr.append([])  # 追加行
        for j in range(length):
            arr[i].append("口")  # 追加列

    row = 0   # 初始值所在行
    col = length // 2   # 初始值所在列

    # 循环绘制正方格，并设置对应的值
    for i in range(1 , length*length+1):

        arr[row][col] = i  # 初始值位置

        # 默认右上角坐标
        row = row - 1
        col = col + 1

        # 定义奇数的倍数设置下一个值在其正下方
        if i % length == 0 :
            col = col - 1
            row = row + 2
        # 当行数向上超出正方格区域，将其设置在最后一行
        elif row < 0 :
            row = length -1
        # 当列数向右超出正方格区域，将其设置在第一列
        elif col >= length :
            col = 0

    # 根据设置好的坐标输出
    for i in range(length):
        for j in range(length):
                print(arr[i][j] , end="\t")
        print("")

#print(arr)
