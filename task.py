def task(a,b,c):
	sum=0
	multi=1
	l=[a,b,c]
	even=[]
	odd=[]
	for i in l:
		if i%2==0:
			even.append(i)
		else:
			odd.append(i)
	if len(even)==3:
		for i in even:
			sum=sum+i
		return(sum)
	elif len(odd)==3:
		for i in odd:
			multi=multi*i
		return(multi)
	elif len(even)==2:
		for i in even:
			sum=sum+i
		s=sum-odd[0]
		return(s)
	else:
		for i in odd:
			sum=sum+i
		s=even[0]-sum
		return(s)
print(task(1,1,1))