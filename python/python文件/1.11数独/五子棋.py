size = input('请输入棋盘大小：')

size = int(size)

arr = []

def initChess(arr):#定义函数
	for i in range(size):
		arr.append([])
		for j in range(size):
			arr[i].append('口')

initChess(arr)


def printChess(arr):
	for i in range(size):
		for j in range(size):
			print(arr[i][j] , end="\t")	
		print('')	

printChess(arr)

#第二个版本
#引入random模块
import random

while True:
	print('用户下棋')

	while True:
		location  = input('请输入要要落子的位置，如 1,1\n')
		value = location.split(',')
		if arr[int(value[0])][int(value[1])] == '口':

			arr[int(value[0])][int(value[1])] = '赢'
			break

		else:
			print('该位置有子了')
			continue

	printChess(arr)

		
	# 接下来电脑下棋
	print('电脑下棋')	
	while True:
		#设置两个随机数作为xy坐标
		intX = random.randint(0,size-1)
		intY = random.randint(0,size-1)	

		#判断给位置是否被占用
		if arr[intX][intY] == '口':

			arr[intX][intY] = '输'

			#结束循环
			break
		else:
			print('该位置有子了')
			#重新循环
			continue

		
	
	printChess(arr)

	#行上面形成五子连珠
	for i in range(size):
		rowStr = ''
		for j in range(size):
			rowStr = rowStr +arr[i][j]

			#查找有没有五个连续一样的
			if rowStr.find('赢赢赢赢赢') != -1:
				print('恭喜你，你赢了电脑!')
				exit()

	#列上面形成五子连珠
	for i in range(size):
		rowStr = ''
		for j in range(size):
			rowStr = rowStr +arr[j][i]

			#查找有没有五个连续一样的
			if rowStr.find('赢赢赢赢赢') != -1:
				print('恭喜你，你赢了电脑!')
				exit()


	#左对角上面形成五子连珠
	for i in range(size):
		row = i
		col = 0

		leftStr = ""
		while row <= size-1: 
			leftStr += arr[row][col]
			row = row + 1
			col = col + 1
			if leftStr.find('赢赢赢赢赢') != -1:
				print('恭喜你，五子连珠')
				exit()


	#右对角上面形成五子连珠
	for i in range(size):
		row = i
		col = 0

		leftStr = ""
		while row >= 0: 
			leftStr += arr[row][col]
			row = row - 1
			col = col + 1
			if leftStr.find('赢赢赢赢赢') != -1:
				print('恭喜你，五子连珠')
				exit()


			





	

