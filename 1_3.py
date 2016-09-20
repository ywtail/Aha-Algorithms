# coding:utf-8
# 快速排序(从小到大)

inputs=map(int,raw_input().split())

n=len(inputs)

def quicksort(left,right):
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
		#print i,j
		if i<j:
			inputs[i],inputs[j]=inputs[j],inputs[i]

	inputs[left],inputs[i]=inputs[i],inputs[left]
	#print inputs
	quicksort(left,i-1)
	quicksort(i+1,right)

quicksort(0,n-1)

for x in inputs:
	print x,