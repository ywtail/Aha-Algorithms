# coding:utf-8
# 简单的桶排序(从大到小)

book=[0 for i in range(1001)]
inputs=map(int,raw_input().split())

for x in inputs:
	book[x]+=1

for i in range(1001)[::-1]:
	if book[i]>0:
		for j in range(book[i]):
			print i,