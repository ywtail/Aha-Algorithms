# coding:utf-8
# 深度优先搜索：炸弹人

n,m,startx,starty=map(int,raw_input().split())
a=[] #存地图
for i in range(n):
	a.append(raw_input())

nex=[[0,1],[1,0],[0,-1],[-1,0]] # 右，下，左，上
book=[[0 for i in range(m)] for j in range(n)] #不走回头路
book[startx][starty]=1 #标记起点已经在路径中

def count_kills(x,y):
	num=0
	tempx=x
	tempy=y
	while a[tempx][tempy]!='#':
		if a[tempx][tempy]=='G':
			num+=1
		tempy+=1
	tempy=y
	while a[tempx][tempy]!='#':
		if a[tempx][tempy]=='G':
			num+=1
		tempx+=1
	tempx=x
	while a[tempx][tempy]!='#':
		if a[tempx][tempy]=='G':
			num+=1
		tempy-=1
	tempy=y
	while a[tempx][tempy]!='#':
		if a[tempx][tempy]=='G':
			num+=1
		tempx-=1
	return num

ma=0
def dfs(x,y):
	global ma
	global printx
	global printy
	tcount=count_kills(x,y)
	if tcount>ma:
		ma=tcount
		printx=x
		printy=y
	for i in range(4):
		tx=x+nex[i][0]
		ty=y+nex[i][1]
		if tx<0 or tx>n-1 or ty<0 or ty>m-1:
			continue
		if book[tx][ty]==0 and a[tx][ty]=='.':
			book[tx][ty]=1
			dfs(tx,ty)
	return

dfs(startx,starty)
print '(%d,%d) %d' %(printx,printy,ma)

'''
input：
13 13 3 3
#############
#GG.GGG#GGG.#
###.#G#G#G#G#
#.......#..G#
#G#.###.#G#G#
#GG.GGG.#.GG#
#G#.#G#.#.#.#
##G...G.....#
#G#.#G###.#G#
#...G#GGG.GG#
#G#.#G#G#.#G#
#GG.GGG#G.GG#
#############

output:
(7,11) 10
'''

