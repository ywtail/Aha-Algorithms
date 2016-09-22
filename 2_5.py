# coding:utf-8
# 数组模拟链表，输入一个数插入正确的位置
# data存数据，right存（下一个数的）索引

data=map(int,raw_input().split())
right=[i for i in range(1,len(data))]+[0]
#print data
#print right
inpt=int(raw_input())
data.append(inpt)

def func():
	for i in xrange(len(data)):
		if data[i]>inpt:
			break
	i-=1
	right.append(right[i])
	right[i]=len(data)-1
	#print data,right
	temp=0
	while right[temp]!=0:
		print data[temp],
		temp=right[temp]
	print data[temp]

func()

# 输入：2 3 5 8 9 10 18 26 32
# 输入：6
