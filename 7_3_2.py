# coding:utf-8
# 最大堆排序：从小到大排序。节点编号从1开始。

# 向下调整，每次跟孩子中较小的那个值交换
def siftdown(i): #i为要调整的节点的编号
	while i*2<=n: #要调整的节点至少有左孩子
		temp=i*2 if h[i*2]>h[i] else i #temp标记值最小的节点编号
		if i*2+1<=n and h[i*2+1]>h[temp]:
			temp=i*2+1 
		if temp!=i:
			h[i],h[temp]=h[temp],h[i]
			i=temp
		else:
			break #已经是堆，不需要调整

# 创建堆：调整二叉树中的节点，从n/2节点开始
def creat():
	for i in range(1,n/2+1)[::-1]:
		siftdown(i) 

# 每次将最大的（堆顶）调整到最后，堆大小-1
def heapsort():
	global n
	for i in range(num-1):
		h[1],h[n]=h[n],h[1]
		n-=1
		siftdown(1)

num=int(raw_input())		
h=map(int,raw_input().split()) #放入完全二叉树
h.insert(0,0) #为了方便计算，输入值从1开始编号

n=num

creat() #创建堆
print h

heapsort()
print h[1:]

'''
input：
14
99 5 36 7 22 17 46 12 2 19 25 28 1 92

output:
[0, 99, 25, 92, 12, 22, 28, 46, 7, 2, 19, 5, 17, 1, 36]
[1, 2, 5, 7, 12, 17, 19, 22, 25, 28, 36, 46, 92, 99]
'''