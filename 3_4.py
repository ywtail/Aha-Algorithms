# coding:utf-8
# 枚举：数的全排列

import itertools

def myfunc():
	temp=list(itertools.permutations('123'))
	for x in temp:
		print ''.join(x)
	#print len(temp)

#myfunc()

for a in xrange(1,4):
	for b in xrange(1,4):
		for c in xrange(1,4):
			if a!=b and a!=c and b!=c:
				print "%d%d%d" %(a,b,c)
