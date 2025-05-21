def reverse_string():
	a=str(input("Enter the string : "))
	b=len(a)
	c=a[-1:-(b+1):-1]
	return(c)
print(reverse_string())