# coding:utf-8
# 二分图最大匹配

n,m=map(int,raw_input().split())
e=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(m):
	x,y=map(int,raw_input().split())
	e[x][y]=1
	e[y][x]=1

match=[0 for i in range(n+1)]

def dfs(u):
	for i in range(1,n+1):
		if book[i]==0 and e[u][i]==1:
			book[i]=1
			if match[i]==0 or dfs(match[i]):
				match[i]=u #更新配对关系
				match[u]=i
				return 1
	return 0

s=0
for i in range(1,n+1):
	book=[0 for j in range(1+n)] #清空上次搜索时的标记
	if dfs(i): #如果找到增广路，配对数加1
		s+=1
print s

"""
6 5
1 4
1 5
2 5
2 6
3 4

3
"""
