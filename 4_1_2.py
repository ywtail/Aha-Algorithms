# coding:utf-8
# 深度优先搜索：_ _ _ + _ _ _ = _ _ _

n=int(raw_input())
book=[0 for i in range(n+1)]
temp=[0 for i in range(n+1)]
total=0

def dfs(step):
	global total
	if step==(n+1):
		if (temp[1]+temp[4])*100+(temp[2]+temp[5])*10+temp[3]+temp[6]==temp[7]*100+temp[8]*10+temp[9]:
			total+=1
			print "%d%d%d+%d%d%d=%d%d%d" %(temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9])
		return
	for i in range(1,n+1):
		if book[i]==0:
			temp[step]=i
			book[i]=1
			dfs(step+1)
			book[i]=0
	return

dfs(1)
print total/2

# total/2=168