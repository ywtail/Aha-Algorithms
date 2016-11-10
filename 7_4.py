# coding:utf-8
# 并查集：求一共有几个犯罪团伙

def getf(v):
	if f[v]==v:
		return v
	else:
		f[v]=getf(f[v]) #路径压缩，顺带把经过的节点改为祖先的值
		return f[v]

def merge(v,u):
	t1=getf(v)
	t2=getf(u)
	if t1!=t2:
		f[t2]=t1

n,m=map(int,raw_input().split())
f=[i for i in range(n+1)]

for i in range(m):
	x,y=map(int,raw_input().split())
	merge(x,y)

ans=0

#扫描有多少个犯罪团伙
for i in range(1,n+1):
	if f[i]==i:
		ans+=1
print ans

'''
input：
10 9
1 2
3 4
5 2
4 6
2 6
8 7
9 7
1 6
2 4

output:
3

分析：
每次找到祖先，修改祖先对应值。路径中节点对应值通过下一次经过时路径压缩改变。
'''