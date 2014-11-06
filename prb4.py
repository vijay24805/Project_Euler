"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time


"""
Storing all three digit numbers
"""
def three_digit_num():
    number=[]
    for n in range(100,1000):
        number.append(n)
    return number

"""
Find all the products of two digit numbers
"""
def product_of_num():
    num=[]
    product=[]
    num=three_digit_num()
    for n in num:
        for x in num:
            product.append(n*x)
    return product

"""
Find the largest palindrome number from the list

"""

def find_palindrome():
    each_product=[]
    each_product=product_of_num()
    palindrome_num=[]
    for x in each_product:
        str_value=str(x)
        temp1=temp2=[] # Used to compare a number to its reverse
        for digit in str_value:
            temp1.append(digit)
        temp2=list(temp1)
        temp1.reverse()
        if cmp(temp1,temp2)==0:
            palindrome_num.append(int(''.join(temp2)))
    return max(palindrome_num)





if __name__ == "__main__":
	start = time.clock()
	three_digit_num()
	product_of_num()
	print find_palindrome()
	print "Time taken - " + str(time.clock() - start)


	
