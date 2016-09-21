# coding:utf-8
# 桟（判断回文：先求中间，然后前半部分压入栈，弹出与后半部分对比。）

s=raw_input()
n=len(s)

def func():
	if s==s[::-1]:
		print "YES"
	else:
		print "NO"
		
#func()

if n==1:
	print "YES"
else:
	mid=n/2
	mids=""
	for i in xrange(mid):
		mids+=(s[i])

	if n%2==0:
		nex=mid
	else:
		nex=mid+1

	for j in xrange(nex,n):
		if mids[i]!=s[j]:
			break
		i-=1

	if i==-1:
		print "YES"
	else:
		print "NO"

# 输入：ahaha
# 输出：YES