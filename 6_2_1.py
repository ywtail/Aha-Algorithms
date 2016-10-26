# coding:utf-8
# Dijkstra算法：单源最短路径。求顶点1到其他顶点的最短路径。

n,m=map(int,raw_input().split())
inf=999999
e=[[inf for i in range(n+1)] for i in range(n+1)]
for i in range(n):
	e[i+1][i+1]=0
for i in range(m):
	a,b,c=map(int,raw_input().split())
	e[a][b]=c
dis=[0 for i in range(n+1)]
for i in range(1,n+1): #初始化dis列表
	dis[i]=e[1][i]
book=[0 for i in range(n+1)]
book[1]=1

for i in range(1,n+1):
	mi=inf #找到离1号顶点距离最近的点
	for j in range(1,n+1):
		if book[j]==0 and dis[j]<mi:
			mi=dis[j]
			u=j
	book[u]=1
	for v in range(1,n+1):
		if e[u][v]<inf and dis[v]>dis[u]+e[u][v]:
			dis[v]=dis[u]+e[u][v]

for i in range(1,n+1):
	print dis[i],
			
'''
input：
6 9
1 2 1
1 3 12
2 3 9
2 4 3
3 5 5
4 3 4
4 5 13
4 6 15
5 6 4

output:
0 1 8 4 13 17

'''

# 用邻接矩阵存，时间复杂度O(N^2)，不能有负权边。
# 基于贪心策略，每次扩展路径最短的点，更新与其相邻的点的路程。
# M远小于N^2的图称为稀疏图，而M相对较大的图称为稠密图
# 对于变数M少于N^2的稀疏图来说，用邻接表代替邻接矩阵，时间复杂度O(M+N)logN
# M在最坏情况下是N^2，复杂度比邻接矩阵大。
