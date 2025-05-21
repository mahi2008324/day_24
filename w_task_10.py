#Write a Python program to find Average of Numbers in a List? Using functions 
a=input("Enter the list numbers by separating by spaces : ").split( )
def average():
	sum=0
	for i in a:
		sum=sum+int(i)
	avg=sum/len(a)
	return(avg)
print(average())