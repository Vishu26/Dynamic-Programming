### Given sum p, find if rod can be cut to generate sum p - There may be extra pieces remaining ###

def generate(a,n,su):
    d =[[0]*(n+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1:
                d[i][j]=[[a[i-1]*j,[i]*j]]
            elif j<i:
                d[i][j]=d[i-1][j]
            elif i==j:
                d[i][j]=[[a[i-1],[i]]]+d[i-1][j]
            else:
                b=[]
                for p in d[i][j-i]:
                    b.append([p[0]+a[i-1],p[1]+[i]])
                d[i][j]=b+d[i-1][j]
    for i in range(1,n+1):
        for j in d[i][i]:
        	if j[0]==su:
        		yield j[1]
if __name__=='__main__':
	n=int(input('Enter the length of the rod : '))
	a=list(map(int,input('Enter the price array (use space) : ').split()))
	su=int(input('Enter the expected price : '))
	ans=generate(a,n,su)
	if not ans:
		print('Not possible')
	else:
		print('The possible pieces are : ')
		for i in ans:
			print(i)


