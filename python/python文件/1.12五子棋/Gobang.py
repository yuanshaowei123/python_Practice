#第一步
#设置棋盘大小

print('请输入一个大于1的奇数开启数独游戏')

size = input('请输入：')

size = int(size)

arr = []

#绘制棋盘
def drawChess(size):
	for i in range(size):
		arr.append([])
		for j in range(size):
			arr[i].append('口')

drawChess(size)	


#打印棋盘
def printChess(size):
	for i in range(size):
		for j in range(size):
			print(arr[i][j] , end='\t')
		print()
printChess(size)


#第二步，设置如何落子
while True:
	#引入随机数模块
	import random

	print('用户下棋')
	while True:
		user = input('请您输入落子位置，如 1,1\n')

		user = user.split(',')
		if arr[int(user[0])][int(user[1])] == '口':

			arr[int(user[0])][int(user[1])] = '赢'

			printChess(size)

			break
		else:
			print('该位置被占用')

			continue

		

	#电脑下棋
	print('电脑下棋')
	while True:
		initX = random.randint(0,size-1)

		initY = random.randint(0,size-1)
		if arr[initX][initY] == '口':

			arr[initX][initY] = '输'

			printChess(size)

			break

		else:
			continue


	#判断输赢

	#行上面形成五子连珠
	for i in range(size):
		rowStr = ''
		for j in range(size):
			rowStr = rowStr + arr[i][j]

			if rowStr.find('赢赢赢赢赢') != -1:

				print('恭喜您，行上面形成五子连珠')

				exit()

	#列上面形成五子连珠
	for i in range(size):
		colStr = ''
		for j in range(size):
			colStr += arr[j][i]

			if colStr.find('赢赢赢赢赢') != -1:

				print('恭喜您，列上面形成五子连珠')
				
				exit()

	#交叉线形成五子连珠
	#左下五子连珠
	for i in range(size):
		row = i
		col = 0

		leftStr = ''
		while row <= size-1:
			leftStr = leftStr + arr[row][col] 
			row = row +1
			col = col +1

			if leftStr.find('赢赢赢赢赢') != -1:

				print('恭喜您，左下五子连珠')

				exit()

	#右上五子连珠
	for i in range(size):
		row = i
		col = 0

		rightStr = ''
		while row >0:
			rightStr = leftStr + arr[row][col] 
			row = row - 1
			col = col - 1

			if rightStr.find('赢赢赢赢赢') != -1:
				
				print('恭喜您，右上五子连珠')

				exit()

		




	

		