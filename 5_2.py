# coding:utf-8
# 城市地图：DFS，找最短路径

n,m=map(int,raw_input().split()) #顶点与边个数
e=[[9999999 for i in range(n+1)] for i in range(n+1)] #图存入邻接矩阵
for i in range(1,n+1):
	e[i][i]=0
for i in range(m):
	a,b,c=map(int,raw_input().split())
	e[a][b]=c
book=[0 for i in range(n+1)]

mi=9999999
t=[] #记录路径
def dfs(cur,dis):
	global mi
	t.append(cur)
	if dis>mi: #如果当前dis>mi，直接返回
		return
	if cur==5:
		if dis<mi:
			mi=dis
			print t,dis
		return
	for i in range(1,n+1):
		if book[i]==0 and e[cur][i]>0 and e[cur][i]<9999999:
			book[i]=1
			dfs(i,dis+e[cur][i])
			book[i]=0
			t.pop()
	return

book[1]=1
dfs(1,0)
print mi
			
'''
input：
5 8
1 2 2
1 5 10
2 3 3
2 5 7
3 1 4
3 4 4
4 5 5
5 3 3

output:
[1, 2, 3, 4, 5] 14
[1, 2, 5] 9
9
'''

