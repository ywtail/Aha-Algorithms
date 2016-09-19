# coding:utf-8
# 冒泡排序(从大到小)

inputs=map(int,raw_input().split())
n=len(inputs)

for i in xrange(0,n-1):
	for j in xrange(0,n-1-i):
		if inputs[j]<inputs[j+1]:
			inputs[j],inputs[j+1]=inputs[j+1],inputs[j]

for x in inputs:
	print x,