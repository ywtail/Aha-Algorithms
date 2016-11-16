# coding:utf-8
# 图的割点：邻接矩阵存，O(N^2)，使用邻接表O(N+M)

n,m=map(int,raw_input().split())
e=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(m):
	x,y=map(int,raw_input().split())
	e[x][y]=1
	e[y][x]=1

index=0
num=[0 for i in range(n+1)]
low=[0 for i in range(n+1)]
flag=[0 for i in range(n+1)]
root=1

def dfs(cur,father):
	global index
	index+=1
	child=0
	num[cur]=index #当前顶点时间戳
	low[cur]=index #当前顶点能够访问到的最早顶点时间戳，即自己的时间戳
	for i in range(1,n+1):
		if e[cur][i]==1:
			if num[i]==0: #时间戳为0，,还未被访问过
				child+=1
				dfs(i,cur)
				low[cur]=min(low[cur],low[i]) #更新当前顶点cur能访问到的组早顶点的时间戳
				if cur!=root and low[i]>=num[cur]: #不能回到祖先
					flag[cur]=1
				if cur==root and child==2:
					flag[cur]=1
			elif i!=father:
				low[cur]=min(low[cur],num[i])

dfs(1,root)
for i in range(1,n+1):
	if flag[i]==1:
		print i,

"""
6 7
1 4
1 3
4 2
3 2
2 5
2 6
5 6

2
"""
