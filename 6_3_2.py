# coding:utf-8
# Bellman-ford: 优化，检测是否有负权回路。

inf=999999999
n,m=map(int,raw_input().split())
u=[0 for i in range(n+1)]
v=[0 for i in range(n+1)]
w=[0 for i in range(n+1)]
for i in range(1,m+1):
	u[i],v[i],w[i]=map(int,raw_input().split())

# 初始化dis数组，这里是1号顶点到其余各个顶点初始路程
dis=[inf for i in range(n+1)]
dis[1]=0

# 进行n-1轮松弛，每次松弛枚举m条边
for k in range(n-1):
	check=1
	for i in range(1,m+1):
		if dis[v[i]]>dis[u[i]]+w[i]:
			dis[v[i]]=dis[u[i]]+w[i]
			check=0
	if check:
		break

# 检测负权回路
for i in range(1,m+1):
	if dis[v[i]]>dis[u[i]]+w[i]:
		print "You Fuquan Huilu"
	
print dis[1:]		

'''
input：
5 5
2 3 2
1 2 -3
1 5 5
4 5 2
3 4 3

output:
[0, -3, -1, 2, 4]

分析：
算法经常会在未达到n-1轮松弛前就已经计算出最短路径。
书：因此可以添加一个列表备份dis，如果在新一轮松弛中dis不变，可以提前跳出循环。
其实不用备份列表，只要用check标记就行，只要修改dis就将chek置0。
'''