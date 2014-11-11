


def prime_factors():
	prime=[]	
	for n in range(2,21):
		for i in range(2,21):
			if(n%i==0):
				if(i==n):
					continue
				else:
					break
			else:
				if(i==20):
					prime.append(n)
				else:
					continue
	return prime
			


if __name__=="__main__":
	print prime_factors()