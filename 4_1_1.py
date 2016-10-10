# coding:utf-8
# 深度优先搜索：全排列

n=int(raw_input())
book=[0 for i in range(n+1)]
temp=[0 for i in range(n+1)]

def dfs(step):
	if step==(n+1):
		print ''.join(map(str,temp))[1:]
		return
	for i in range(1,n+1):
		if book[i]==0:
			temp[step]=i
			book[i]=1
			dfs(step+1)
			book[i]=0
	return

dfs(1)

# $ python 4_1_1.py
# 3
# 123
# 132
# 213
# 231
# 312
# 321