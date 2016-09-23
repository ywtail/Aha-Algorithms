# coding:utf-8
# _ _ _ + _ _ _ = _ _ _ 1-9各出现一次。173+286=459与286+173=459相同。
# 以下使用枚举，时间复杂度太高，运行时间过长

def enumerate():
	count=0
	a=[0 for i in range(10)]
	for a[1] in xrange(1,10):
		for a[2] in xrange(1,10):
			for a[3] in xrange(1,10):
				for a[4] in xrange(1,10):
					for a[5] in xrange(1,10):
						for a[6] in xrange(1,10):
							for a[7] in xrange(1,10):
								for a[8] in xrange(1,10):
									for a[9] in xrange(1,10):
										book=[0 for i in range(10)]
										for i in xrange(1,10):
											book[a[i]]=1
										if sum(book)==9 and (a[1]+a[4])*100+(a[2]+a[5])*10+a[3]+a[6]==a[7]*100+a[8]*10+a[9]:
											count+=1

	print count/2


# _ _ + _ _ = _ _ 取值1-9

count=0
a=[0 for i in range(7)]
for a[1] in xrange(1,10):
	for a[2] in xrange(1,10):
		for a[3] in xrange(1,10):
			for a[4] in xrange(1,10):
				for a[5] in xrange(1,10):
					for a[6] in xrange(1,10):
						book=[0 for i in range(10)]
						for i in xrange(1,7):
							book[a[i]]=1
						if sum(book)==6 and (a[1]+a[3])*10+a[2]+a[4]==a[5]*10+a[6]:
							count+=1
							print "%d%d+%d%d=%d%d" %(a[1],a[2],a[3],a[4],a[5],a[6])

print count/2

# 输出：200