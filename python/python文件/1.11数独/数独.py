'''
   游戏规则
   1.第一个数字放在第一行中间
   2.如果是输入的数字的倍数，放在这个数的下面，不用遵守规则
   3.如果超出行，折回来放入最后一行
     如果超出列，折回来放入第一列
'''
while True: #可以重复运行
	print('请输入一个大于1的奇数开启数独游戏')

	#定义一个数字
	num = input('请输入：')

	#判断输入的是不是exit
	if 'exit' == num:
		break

    #判断输入的是不是数字
	if not num.isdigit():
		print('输入的不是数字')
		continue

	#定义为整形
	num = int(num)

	if num == 1:
		continue

	#判断输入的是不是奇数
	if num % 2 == 0:
		print('输入的不是奇数')
		continue

	#定义空数组
	arr = []

	#循环出行和列的数组
	for i in range(num):
		arr.append([])
		for j in range(num):
			arr[i].append('口')

	#定义第一个数的位置行和列
	row = 0
	col = num // 2

	#定义行和列的内容
	for i in range(1,num*num+1):
        #将i放到列表中
		arr[row][col] = i

		#设置下一个i的位置
		if i % num == 0:
			row = row + 1
			col = col
		else:
			row = row - 1
			col = col + 1

        #若超出行，折回放在最后一行
		if row < 0:
			row = num-1
        
        #若超出列，折回放在第一列
		if col > num-1:
			col = 0

	#输出行和列的内容
	for i in range(num):
		for j in range(num):
			print(arr[i][j] , end='\t')
		print('')

	

	
    
