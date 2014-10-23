"""
Problem:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
def prime_factor():
	i=600851475143
	factors=[] #list stores all the factors of a number
	for n in xrange(2,i):
		if(i%n==0 and (n%2!=0 and n!=2)):
			i/=n
			factors.append(n)
			if(i==1):
				break
	
	"""
	Now I have all the factors(which are not even numbers)

	Next step is to find prime number from factors list
	"""

	for factor in factors:
		sqr_root=int(math.sqrt(factor))
		"""
		I take a factor from list and divide it by numbers from 3
		to sqroot(factor-1).If I get a 0 as remainder I consider it
		as non prime and remove from the list.I apply this only to
		factors whose sqr root is greater than 3.If it is less than 
		3 I divide it by each number between 3 and factor-1.
		"""
		if(sqr_root<=3):
			for num in range(3,factor-1):
				if(factor%num==0):
					factors.remove(factor)
					break
		else:
			for num in range(3,sqr_root):
				if(factor%num==0):
					factors.remove(factor)
					break
	return max(factors)
	

if __name__ == "__main__":
	print prime_factor()

	 

