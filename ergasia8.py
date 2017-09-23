
#a8roisma pollaplasiwn tou n ws m

sum=0

def is_multiple(m,n): #pairnei tous m kai n
	
	def multiples(n,count):
		for i in range(count):			
			print(i*n) #pollaplasia tou n
			
		while(multiples>0 && multiples<=m): #mexri kai to m
			sum += multiples #athroisma twn pollaplasiwn
			
		print("The sum is",sum)

