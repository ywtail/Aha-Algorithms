# coding:utf-8
# 队列（解密qq号：第一个弹出，第二个放末尾...head记录队首，tail记录队尾下一位）

inputs=map(int,raw_input().split())
n=len(inputs)

def func():
	while inputs:
		print inputs.pop(0),
		if inputs:
			inputs.append(inputs[0])
			inputs.pop(0)

#func()

head=0
tail=n
while head<tail:
	print inputs[head],
	head+=1
	if head<tail:
		inputs.append(inputs[head])
		tail+=1
		head+=1


# 输入：6 3 1 7 5 8 9 2 4
# 输出：6 1 5 9 4 7 2 8 3