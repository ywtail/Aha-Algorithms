# coding:utf-8
# Prime：最小生成树，O(N^2)

inf=99999999
n,m=map(int,raw_input().split())

#用二维列表存
e=[[inf for i in range(n+1)] for j in range(n+1)]

for i in range(m):
	u,v,w=map(int,raw_input().split())
	e[u][v]=w
	e[v][u]=w

dis=[inf for i in range(n+1)]
for i in range(1,n+1):
	e[i][i]=0 #对角线置0
	dis[i]=e[1][i] #任意选一个点（这里选1）

book=[0 for i in range(n+1)]
book[1]=1
c=1
s=0
while c<n:
	#选book=0且dis最小的，将这个点加入被选中的集合，book置1
	mi=inf
	for i in range(1,n+1):
		if book[i]==0 and dis[i]<mi:
			mi=dis[i]
			t=i
	book[t]=1
	c+=1
	s+=dis[t]

	#根据上方被选中的t，更新dis
	for i in range(1,n+1):
		if book[i]==0 and e[t][i]<dis[i]:
			dis[i]=e[t][i]

print s

"""
6 9
2 4 11
3 5 13
4 6 3
5 6 4
2 3 6
4 5 7
1 2 1
3 4 9
1 3 2

19
"""
