# coding:utf-8
# 桟和队列应用：小猫钓鱼（书中不符合常识，从上往下一张张收（模拟桟），少收了一张牌，以下根据书中思路，收牌时从上往下一张张收，但是不漏收牌）

a=map(int,raw_input().split())
b=map(int,raw_input().split())

#c=[]
def funcone(a,b,c):
	while a and b:
		c.append(a[0])
		a.pop(0)
		atemp=c.index(c[-1])
		if atemp!=(len(c)-1):
			a+=c[atemp:][::-1]
			c=c[:atemp]
		#print a,b
		#print c
		if a:
			c.append(b[0])
			b.pop(0)
			btemp=c.index(c[-1])
			if btemp!=(len(c)-1):
				b+=c[btemp:][::-1]
				c=c[:btemp]
			#print a,b
			#print c
	if a:
		print "a win"
		print a,c
	else:
		print "b win"
		print b,c

#funcone(a,b,c)

def functwo():
	c=[0 for i in range(100)]
	astart=0
	aend=len(a)
	bstart=0
	bend=len(b)
	top=0
	book=[0 for i in range(1,10)]

	while astart<aend and bstart<bend:
		t=a[astart]
		if book[t]==0:
			top+=1
			c[top]=t
			astart+=1
			book[t]=1
			#print a,b,book
			#print top
		else:
			book[t]=0
			astart+=1
			a.append(t)
			aend+=1
			while c[top]!=t:
				book[c[top]]=0
				a.append(c[top])
				aend+=1
				top-=1
			a.append(c[top])
			aend+=1
			top-=1
			#print a,b,book
			#print top
		t=b[bstart]
		if astart<aend and bstart<bend:
			if book[t]==0:
				top+=1
				c[top]=t
				bstart+=1
				book[t]=1
				#print a,b,book
				#print top
			else:
				book[t]=0
				bstart+=1
				b.append(t)
				bend+=1
				while c[top]!=t:
					book[c[top]]=0
					b.append(c[top])
					bend+=1
					top-=1
				b.append(c[top])
				bend+=1
				top-=1
				#print a,b,book
				#print top

	if astart==aend:
		print "b wins"
		for i in xrange(bstart,bend):
			print b[i],
	else:
		print "a wins"
		for i in xrange(astart,aend):
			print a[i],
	print "\n"
	for j in xrange(1,top+1):
			print c[j],

functwo()
# 2 4 1 2 5 6
# 3 1 3 5 6 4
#输出：
#1 6 5 2 3 4 1
#3 4 5 6 2