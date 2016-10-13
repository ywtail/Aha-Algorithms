# coding:utf-8
# 广度优先搜索：宝岛探险（题中编号从1开始，这里从0开始），求所在岛屿面积

n,m,startx,starty=map(int,raw_input().split())
a=[] #存地图
for i in range(n):
	a.append(raw_input().split())

nex=[[0,1],[1,0],[0,-1],[-1,0]] # 右，下，左，上
book=[[0 for i in range(m)] for j in range(n)] #不走回头路
book[startx][starty]=1 #标记起点已经在路径中
que=[[startx,starty]]
head=0
tail=0
count=1

while head<=tail:
	for i in range(4):
		tx=que[head][0]+nex[i][0]
		ty=que[head][1]+nex[i][1]
		if tx<0 or tx>n-1 or ty<0 or ty>m-1:
			continue
		if book[tx][ty]==0 and a[tx][ty]!='0':
			book[tx][ty]=1
			que.append([tx,ty])
			tail+=1
			count+=1
	head+=1

print count

'''
input：
10 10 5 7
1 2 1 0 0 0 0 0 2 3
3 0 2 0 1 2 1 0 1 2
4 0 1 0 1 2 3 2 0 1
3 2 0 0 0 1 2 4 0 0
0 0 0 0 0 0 1 5 3 0
0 1 2 1 0 1 5 4 3 0
0 1 2 3 1 3 6 2 1 0
0 0 3 4 8 9 7 5 0 0
0 0 0 3 7 8 6 0 1 2
0 0 0 0 0 0 0 0 1 0

output:
38
'''

