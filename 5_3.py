# coding:utf-8
# BFS：无向地图中求最少转机次数
# 广度优先更适用于所有边权值相同的情况

n,m,start,end=map(int,raw_input().split()) #顶点与边个数
e=[[9999999 for i in range(n+1)] for i in range(n+1)] #图存入邻接矩阵
for i in range(1,n+1):
	e[i][i]=0
for i in range(m):
	a,b=map(int,raw_input().split())
	e[a][b]=1
	e[b][a]=1
book=[0 for i in range(n+1)]

que=[[start,0]]
book[start]=1
head=0
tail=1
flag=0

while head<tail:
	cur=que[head][0]
	for i in range(1,n+1):
		if book[i]==0 and e[cur][i]==1:
			book[i]=1
			que.append([i,que[head][1]+1])
			tail+=1
		if que[tail-1][0]==end: #只要扩展到目标结点5就终止
			flag=1
			break
	if flag:
		print que[tail-1][1]
		break
	head+=1

print "que =",que	
print "head =",head

			
'''
input：
5 7 1 5
1 2
1 3
2 3
2 4
3 4
3 5
4 5

output:
2
que = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2]]
head = 2
'''

