# coding:utf-8
# 排序（去除重复数据）
# 桶排序bucketsort()需要知道数值范围，假设需要排序的数<1000

inputs=map(int,raw_input().split())
n=len(inputs)

def newPrint(inputs):
	print inputs[0],
	for k in xrange(1,n):
		if inputs[k]!=inputs[k-1]:
			print inputs[k],

def bucketSort():
	alist=[0 for i in range(1001)]
	outputs=[]
	for x in inputs:
		alist[x]+=1
	for i in xrange(len(alist)):
		if alist[i]>0:
			for j in xrange(alist[i]):
				outputs.append(i)
	newPrint(outputs)

def bubbleSort():
	for i in xrange(n-1):
		for j in xrange(n-1-i):
			if inputs[j]>inputs[j+1]:
				inputs[j],inputs[j+1]=inputs[j+1],inputs[j]
	#print inputs
	newPrint(inputs)

def quickSort(left,right):
	if left>right:
		return
	base=inputs[left]
	i=left
	j=right
	while i!=j:
		while inputs[j]>=base and i<j:
			j-=1
		while inputs[i]<=base and i<j:
			i+=1
		if i<j:
			inputs[i],inputs[j]=inputs[j],inputs[i]
	inputs[left],inputs[i]=inputs[i],inputs[left]
	#print inputs
	quickSort(left,i-1)
	quickSort(i+1,right)

#bucketSort()

#bubbleSort()

quickSort(0,n-1)
newPrint(inputs)

# 输入：20 40 32 67 40 20 89 300 400 15
# 输出：15 20 32 40 67 89 300 400