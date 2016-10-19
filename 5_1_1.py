# coding:utf-8
# 图遍历：DFS

n,m=map(int,raw_input().split()) #顶点与边个数
e=[[9999999 for i in range(n+1)] for i in range(n+1)] #图存入邻接矩阵
for i in range(1,n+1):
	e[i][i]=0
for i in range(m):
	a,b=map(int,raw_input().split())
	e[a][b]=1
	e[b][a]=1
book=[0 for i in range(n+1)]

count=0
def dfs(cur):
	print cur,
	book[cur]=1
	global count
	count+=1
	if count==n: #访问的点数达到n就退出
		return
	for i in range(1,n+1):
		if e[cur][i]==1 and book[i]==0:
			dfs(i)
	return

dfs(1)

'''
input：
5 5
1 2
1 3
1 5
2 4
3 5

output:
1 2 4 3 5
'''

