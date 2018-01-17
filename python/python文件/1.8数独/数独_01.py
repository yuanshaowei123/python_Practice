# 暂时写出来格式
# 设置变量
print('请输入一个奇数，会出现相应的数独')
content = input('请输入：')
# 转换为整形
length = int(content)
arr = []
for i in range(length):
    arr.append([])
    for j in range(length):
        arr[i].append('口')

# for i in range(length):
#     for i in range(length):
#         print(arr[i][j] , end=" ")
#     print("")
col = length // 2 
print(col)

