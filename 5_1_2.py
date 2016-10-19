# coding:utf-8
# 图遍历：BFS

n,m=map(int,raw_input().split()) #顶点与边个数
e=[[9999999 for i in range(n+1)] for i in range(n+1)] #图存入邻接矩阵
for i in range(1,n+1):
	e[i][i]=0
for i in range(m):
	a,b=map(int,raw_input().split())
	e[a][b]=1
	e[b][a]=1
book=[0 for i in range(n+1)]
que=[]

def my_bfs():
	index=0
	book[1]=1
	que.append(1)
	while len(que)<n:
		for i in range(1,n+1):
			if e[que[index]][i]==1 and book[i]==0:
				book[i]=1
				que.append(i)
		index+=1
	print que
#my_bfs()

head=0
que=[1]
tail=1
book[1]=1
while head<tail:
	cur=que[head]
	#if tail>n-1: #写到这里计算步骤更少，但就与my_bfs()思路相同了
	#	break	  
	for i in range(1,n+1):
		if tail>n-1:
			break
		if e[cur][i]==1 and book[i]==0:
			book[i]=1
			que.append(i)
			tail+=1
	head+=1
for k in que:
	print k,
			
'''
input：
5 5
1 2
1 3
1 5
2 4
3 5

output:
1 2 3 5 4
'''

