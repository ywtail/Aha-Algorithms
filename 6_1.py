# coding:utf-8
# Floyd-Warshall：多源最短路径（求任意两点之间最短路径），有向图
# 不能解决带有“负权回路”的图，因为这种图没有最短路径。

n,m=map(int,raw_input().split())
e=[[999999 for i in range(n+1)] for i in range(n+1)]
for i in range(n):
	e[i+1][i+1]=0
for i in range(m):
	a,b,c=map(int,raw_input().split())
	e[a][b]=c

for k in range(1,n+1): #经过顶点k
	for i in range(1,n+1):
		for j in range(1,n+1):
			if e[i][k]<999999 and e[k][j]<999999 and e[i][k]+e[k][j]<e[i][j]:
				e[i][j]=e[i][k]+e[k][j]

for i in range(1,n+1):
	for j in range(1,n+1):
		print e[i][j],
	print ""
			
'''
input：
4 8
1 2 2
1 3 6
1 4 4
2 3 3
3 1 7
3 4 1
4 1 5
4 3 12

output:
0 2 5 4
9 0 3 4
6 8 0 1
5 7 10 0

'''

