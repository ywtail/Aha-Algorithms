# coding:utf-8
# Bellman-ford：单源最短路径，解决负权边。求从1号顶点到其余各点最短路程。
# 时间复杂度O(NM)

inf=999999999
n,m=map(int,raw_input().split())
u=[0 for i in range(n+1)]
v=[0 for i in range(n+1)]
w=[0 for i in range(n+1)]
for i in range(1,m+1):
	u[i],v[i],w[i]=map(int,raw_input().split())

# 初始化dis数组，这里是1号顶点到其余各个顶点初始路程
dis=[inf for i in range(n+1)]
dis[1]=0

# 进行n-1轮松弛，每次松弛枚举m条边
for k in range(n-1):
	for i in range(1,m+1):
		if dis[v[i]]>dis[u[i]]+w[i]:
			dis[v[i]]=dis[u[i]]+w[i]
	
print dis[1:]		

'''
input：
5 5
2 3 2
1 2 -3
1 5 5
4 5 2
3 4 3

output:
[0, -3, -1, 2, 4]

分析：
第1 轮松弛得到的是从1号顶点“只能经过一条边”到达的其余各顶点的最短路径长度。
第2轮得到的是从1号顶点“最多经过两条边”到达其余个顶点的最短路径长度。
如果进行k轮，得到的就是1号顶点“最多经过k条边”到达其余各项顶点的最短路径长度。
所以需要进行n-1轮。在有n个顶点的图中，任意两点之间的最短路径最多包含n-1条边。
'''