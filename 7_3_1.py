# coding:utf-8
# 堆与最小堆排序：从小到大排序。节点编号从1开始。

# 向下调整，每次跟孩子中较小的那个值交换
def siftdown(i): #i为要调整的节点的编号
	while i*2<=n: #要调整的节点至少有左孩子
		temp=i*2 if h[i*2]<h[i] else i #temp标记值最小的节点编号
		if i*2+1<=n and h[i*2+1]<h[temp]:
			temp=i*2+1 
		if temp!=i:
			h[i],h[temp]=h[temp],h[i]
			i=temp
		else:
			break #已经是堆，不需要调整


# 向上调整，每次跟父节点比较
def siftup(i):
	while i/2>0:
		if h[i]<h[i/2]:
			h[i],h[i/2]=h[i/2],h[i] 
			i=i/2
		else:
			break

# 创建堆：调整二叉树中的节点，从n/2节点开始
def creat():
	for i in range(1,n/2+1)[::-1]:
		siftdown(i) 

# 删除顶部元素，尾部元素放到顶部调整，堆大小-1
def deletetop():
	global n
	temp=h[1]
	h[1]=h[n]
	n-=1
	siftdown(1)
	return temp

num=int(raw_input())		
h=map(int,raw_input().split()) #放入完全二叉树
h.insert(0,0) #为了方便计算，输入值从1开始编号

n=num

creat() #创建堆
print h

# 排序，每次删除顶部（最小），将尾部的元素放到顶部，向下调整
for i in range(num):
	print deletetop(),

'''
input：
14
99 5 36 7 22 17 46 12 2 19 25 28 1 92

output:
[0, 1, 2, 17, 5, 19, 28, 46, 12, 7, 22, 25, 99, 36, 92]
1 2 5 7 12 17 19 22 25 28 36 46 92 99

每次删除最小，插入一个数再删除最小：删除堆顶，将元素插入堆顶向下调整。
每次增加一个元素：插入末尾，向上调整。
建立堆：1.每次siftup,O(NlogN)；2.放入一个完全二叉树再调整,O(N)
堆排序：O(NlogN)，和快排一样
'''