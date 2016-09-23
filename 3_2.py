# coding:utf-8
# 枚举：炸弹人（上下左右四个方位搜索）

n,m=map(int,raw_input().split())
a=[]
for i in xrange(n):
	a.append(raw_input())

maxg=0
for i in xrange(1,n):
	for j in xrange(1,m):
		if a[i][j]==".":
			count=0
			x=i
			y=j
			while a[x][y]!="#":
				if a[x][y]=="G":
					count+=1
				x-=1
			x=i
			while a[x][y]!="#":
				if a[x][y]=="G":
					count+=1
				x+=1
			x=i
			while a[x][y]!="#":
				if a[x][y]=="G":
					count+=1
				y-=1
			y=j
			while a[x][y]!="#":
				if a[x][y]=="G":
					count+=1
				y+=1

			if count>maxg:
				p=i
				q=j
				maxg=count


print "(%d,%d) %d" %(p,q,maxg)

# 输入：
#13 13
#############
#GG.GGG#GGG.#
###.#G#G#G#G#
#.......#..G#
#G#.###.#G#G#
#GG.GGG.#.GG#
#G#.#G#.#.###
##G...G.....#
#G#.#G###.#G#
#...G#GGG.GG#
#G#.#G#G#.#G#
#GG.GGG#G.GG#
#############

# 输出：(9,9) 8