# coding:utf-8
# 邻接表：使用列表实现邻接表。

# 构建邻接表
n,m=map(int,raw_input().split())
u=[0 for i in range(m+1)]
v=[0 for i in range(m+1)]
w=[0 for i in range(m+1)]
first=[-1 for i in range(n+1)]
nex=[0 for i in range(m+1)]
for i in range(1,m+1): #读入边
	u[i],v[i],w[i]=map(int,raw_input().split())
	nex[i]=first[u[i]]
	first[u[i]]=i
print first[1:],nex[1:]

# 遍历每个顶点的边
for i in range(1,n+1):
	k=first[i]
	while k!=-1:
		print u[k],v[k],w[k]
		k=nex[k]

			
'''
input：
4 5
1 4 9
4 3 8
1 2 5
2 4 6
1 3 7

output:
[5, 4, -1, 2] [-1, -1, 1, -1, 3]
1 3 7
1 2 5
1 4 9
2 4 6
4 3 8

'''

# first中，1号顶点的第一条边是编号为5的边（即1 3 7）
# next中，1号顶点，编号为5的边的下一条边编号为3（1 2 5），然后是1 4 9
# 即找到1号顶点的一条边后，剩下的边都可以在next数组中找到

# k=first[1]
# while k!=-1:
# 	print u[k],v[k],w[k]
# 	k=next[k]
# 每个顶点都设置了一个链表，保存了从顶底i出发的所有边的序号。
# 用邻接表存储图的时间复杂度是O(M)，遍历每条边的时间复杂度也是O(M)
# 如果一个图是稀疏图的话，M要远小于N^2。因此稀疏图用邻接表存储更合适。