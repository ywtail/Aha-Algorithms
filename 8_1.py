# coding:utf-8
# 图的最小生成树：镖局运镖

from operator import itemgetter

n,m=map(int,raw_input().split())
e=[]
for i in range(m):
	e.append(map(int,raw_input().split()))

sort_e=sorted(e,key=itemgetter(2)) #按边的值排序

#使用并查集记录是否在一个集合中（构成环）
f=[i for i in range(n+1)]

def getf(v):
	if f[v]==v:
		return v
	else:
		f[v]=getf(f[v])
		return f[v]

def merge(u,v):
	t1=getf(u)
	t2=getf(v)
	if t1!=t2:
		f[t2]=t1
		return 1
	else:
		return 0

c=0 #到n-1条边终止
s=0 #记录最短的路径和

for i in range(m):
	if merge(sort_e[i][0], sort_e[i][1]):
		c+=1
		s+=sort_e[i][2]
	if c==n-1:
		break

print s

'''
input：
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

output:
19

基本思想：
每次选择最短边，直到选了n-1条边，图连通为止。
如果选择的边造成回路，就舍弃
'''