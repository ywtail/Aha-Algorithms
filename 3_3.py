# coding:utf-8
# 枚举：火柴棍等式
# 输入m根火柴棍（m<=24），拼A+B=C

def func(x):
	num=0
	alist=[6,2,5,5,4,5,6,3,7,6] # 0~9需要的火柴棍数
	while x/10!=0:
		num+=alist[x%10]
		x=x/10
	num+=alist[x%10]
	return num

s=0
m=int(raw_input())
temp=(m-4)/2/2 #a,b,c三个数中任意一个数都不会超过temp个1
ma=int('1'*temp)
#print ma
#a,b,c三个数中任意一个数都不会超过temp个1（1需要的棍最少）
#书中a,b的范围都限制在0~11111,可以通过计算减少枚举范围

# 因为0+4=4和4+0=4表示不同的等式，所以我认为还可以优化一点
def myfunc():
	global s
	for a in range(0,ma):
		for b in xrange(0,ma):
			c=a+b
			if func(a)+func(b)+func(c)==m-4:
				if a>b:
					return
				s+=1
				print "%d+%d=%d" %(a,b,c)
				if a!=b:
					s+=1
					print "%d+%d=%d" %(b,a,c)

#myfunc()
# 输入：18
# 输出：
# 0+4=4
# 4+0=4
# 0+11=11
# 11+0=11
# 1+10=11
# 10+1=11
# 2+2=4
# 2+7=9
# 7+2=9
# total=9

for a in range(0,ma):
		for b in xrange(0,ma):
			c=a+b
			if func(a)+func(b)+func(c)==m-4:
				s+=1
				print "%d+%d=%d" %(a,b,c)

print "total=%d" %s #一共拼出s个等式

# 输入：18
# 输出：
# 0+4=4
# 0+11=11
# 1+10=11
# 2+2=4
# 2+7=9
# 4+0=4
# 7+2=9
# 10+1=11
# 11+0=11
# total=9# 

