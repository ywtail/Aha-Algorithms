# coding:utf-8
# 深度优先搜索：解救小哈（题中编号从1开始，这里从0开始）

n,m=map(int,raw_input().split())
a=[] #存迷宫
for i in range(n):
	a.append(raw_input().split())
startx,starty,goalx,goaly=map(int,raw_input().split())

nex=[[0,1],[1,0],[0,-1],[-1,0]] # 右，下，左，上
book=[[0 for i in range(m)] for j in range(n)] #不走回头路
book[startx][starty]=1 #标记起点已经在路径中
mi=9999999

def dfs(x,y,step):
	global mi
	if x==goalx and y==goaly:
		if step<mi:
			mi=step
		return
	for i in range(4):
		tx=x+nex[i][0] #计算下一个点坐标
		ty=y+nex[i][1]

		if tx<0 or tx>n-1 or ty<0 or ty>m-1:
			continue

		if a[tx][ty]=='0' and book[tx][ty]==0:
			book[tx][ty]=1 #标记这个点已经走过
			dfs(tx,ty,step+1) #尝试下一个点
			book[tx][ty]=0 #尝试完毕，取消这个点的标记

	return

dfs(startx,starty,0)
print mi


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

