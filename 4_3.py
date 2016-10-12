# coding:utf-8
# 广度优先搜索：解救小哈（题中编号从1开始，这里从0开始），用队列实现。

n,m=map(int,raw_input().split())
a=[] #存迷宫
for i in range(n):
	a.append(raw_input().split())
startx,starty,goalx,goaly=map(int,raw_input().split())

nex=[[0,1],[1,0],[0,-1],[-1,0]] # 右，下，左，上
book=[[0 for i in range(m)] for j in range(n)] #不走回头路
book[startx][starty]=1 #标记起点已经在路径中

step=0
que=[[startx,starty,step]]
head=0
tail=0
flag=0 #因为要跳出两层循环，所以用flag来break两次，而不是直接break

while head<=tail:
	for i in range(4):
		tx=que[head][0]+nex[i][0]
		ty=que[head][1]+nex[i][1]
		ts=que[head][2]+1 #步数

		if tx<0 or tx>n-1 or ty<0 or ty>m-1:
			continue

		if book[tx][ty]==0 and a[tx][ty]=='0':
			book[tx][ty]=1
			que.append([tx,ty,ts])
			tail+=1

		if tx==goalx and ty==goaly:
			flag=1
			break

	if flag:
		break

	head+=1

print que[tail][2]

'''
input：
5 4
0 0 1 0
0 0 0 0
0 0 1 0
0 1 0 0
0 0 0 1
0 0 3 2

output:
7
'''

