# coding:utf-8
# Bellman-ford的队列优化

inf=999999999
n,m=map(int,raw_input().split())
u=[0 for i in range(m+1)]		
v=[0 for i in range(m+1)]		
w=[0 for i in range(m+1)]		
first=[-1 for i in range(n+1)]		
nex=[0 for i in range(m+1)]
for i in range(1,m+1):
	u[i],v[i],w[i]=map(int,raw_input().split())
	nex[i]=first[u[i]]
	first[u[i]]=i

dis=[inf for i in range(n+1)]
dis[1]=0

book=[0 for i in range(n+1)]
book[1]=1
que=[1]
head=0
tail=1

print first,nex

while head<tail:
	k=first[que[head]]
	while k!=-1:
		if dis[v[k]]>dis[u[k]]+w[k]:
			dis[v[k]]=dis[u[k]]+w[k]
			if book[v[k]]==0:
				book[v[k]]=1
				que.append(v[k])
				tail+=1
		k=nex[k]
	book[que[head]]=0 #有可能再次入队：最短路径变更后
	head+=1

print dis[1:]

'''
input：
5 7
1 2 2
1 5 10
2 3 3
2 5 7
3 4 4
4 5 5
5 3 6

output:
[-1, 2, 4, 5, 6, 7] [0, -1, 1, -1, 3, -1, -1, -1]
[0, 2, 5, 9, 9]

分析：使用邻接表存储，first存1-n号顶点的第一条边，nex存编号为i的边的下一条边。
队列优化关键：只有在前一遍松弛中改变了最短路径估计值的点，
才可能引起邻接点最短路程发生变化。
用队列存放被松弛的点能够降低时间复杂度。最坏情况O(NM)

如果某个点进入队列的次数超过n次，则图中肯定存在负环。
'''