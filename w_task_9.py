n=int(input("Enter the number : "))
def sum_squares():
	sum=0
	for i in range(1,n+1):
		s=i*i
		sum=sum+s
	return(sum)
print(sum_squares())