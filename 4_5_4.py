# coding:utf-8
# 深度优先搜索：宝岛探险（题中编号从1开始，这里从0开始）；
# 求地图中有多少独立小岛，即求图中独立子图的个数。
# 以下算法是Floodfill漫水填充法（种子填充法）

n,m=map(int,raw_input().split())
a=[] #存地图
for i in range(n):
	a.append(map(int,raw_input().split()))

nex=[[0,1],[1,0],[0,-1],[-1,0]] # 右，下，左，上
book=[[0 for i in range(m)] for j in range(n)] #不走回头路

def dfs(x,y,color):
	a[x][y]=color
	for i in range(4):
		tx=x+nex[i][0]
		ty=y+nex[i][1]
		if tx<0 or tx>n-1 or ty<0 or ty>m-1:
			continue
		if book[tx][ty]==0 and a[tx][ty]>0:
			book[tx][ty]=1
			dfs(tx,ty,color)
	return

c=0
for i in range(n):
	for j in range(m):
		if a[i][j]>0:
			book[i][j]=1
			c-=1
			dfs(i,j,c)

print -c
for i in range(n):
	for j in range(m):
		print "%2d" %a[i][j],
	print ""

'''
input：
10 10
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
4
-1 -1 -1  0  0  0  0  0 -2 -2
-1  0 -1  0 -3 -3 -3  0 -2 -2
-1  0 -1  0 -3 -3 -3 -3  0 -2
-1 -1  0  0  0 -3 -3 -3  0  0
 0  0  0  0  0  0 -3 -3 -3  0
 0 -3 -3 -3  0 -3 -3 -3 -3  0
 0 -3 -3 -3 -3 -3 -3 -3 -3  0
 0  0 -3 -3 -3 -3 -3 -3  0  0
 0  0  0 -3 -3 -3 -3  0 -4 -4
 0  0  0  0  0  0  0  0 -4  0
'''

