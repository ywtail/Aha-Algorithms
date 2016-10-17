# coding:utf-8
# 深度优先搜索：水管工游戏（题中编号从1开始，这里从0开始），水管可翻转，输出一条通路

n,m=map(int,raw_input().split())
a=[] #存管道类型
for i in range(n):
	a.append(map(int,raw_input().split()))
book=[[0 for i in range(m)] for j in range(n)]
flag=0
s=[]

def dfs(x,y,front): #当前坐标及进水口方向(1-4,左上右下)
	global flag #如果不设置为global，函数以外flag永远是0
	if x==(n-1) and y==m:
		flag=1
		print "Yes"
		for k in s:
			print k,
		return

	if x<0 or x>n-1 or y<0 or y>m-1:
		return

	if book[x][y]==1:
		return
	book[x][y]=1

	s.append((x,y))

	if a[x][y]==5 or a[x][y]==6:
		if front==1:
			dfs(x,y+1,1)
		elif front==2:
			dfs(x+1,y,2)
		elif front==3:
			dfs(x,y-1,3)
		else:
			dfs(x-1,y,4)

	if a[x][y]>=1 and a[x][y]<=4: 
		if front==1:
			dfs(x+1,y,2)
			dfs(x-1,y,4)
		elif front==2:
			dfs(x,y+1,1)
			dfs(x,y-1,3)
		elif front==3:
			dfs(x+1,y,2)
			dfs(x-1,y,4)
		else:
			dfs(x,y+1,1)
			dfs(x,y-1,3)

	book[x][y]=0
	s.pop()
	return

dfs(0,0,1)
if flag==0:
	print "impossible"

'''
input：
5 4
5 3 5 3
1 5 3 0
2 3 5 1
6 1 1 5
1 5 5 4

output:
Yes
(0, 0) (0, 1) (1, 1) (2, 1) (2, 2) (2, 3) (3, 3) (4, 3)
'''

