#!/usr/bin/python
import math


def SmithTest(n):
	if isPrime(n):
		print ("Prime numbers can't be Smith Numbers!")
	factorsSum = getPrimeFactorsSum(n) #get the sum N's prime factors individual digits
	target = sumNum(n) #get the sum of N's individual digits aka the target
	if getPrimeFactorsSum(n) == sumNum(n):
		print (n, "is a Smith Number!")
	else:
		print (n, "is not a Smith Number!")

def sumNum(n): #Split number into it's individual digits e.g. 913 to [9,1,3] and returns it's sum, [9,1,3] = 9+1+3 = 13
	sum = 0
	for i in str(n):
		sum = sum+int(i)
	return sum

def getPrimeFactorsSum(n): #get the prime factors of a number and return
	sum = 0
	while (n%2 == 0):
		sum = sum+2
		n = n/2
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		while (n%i == 0):
			sum = sum + sumNum(i)
			n = n/i
	if n == 1:
		return sum
	elif isPrime(n):
		sum = sum + sumNum(int(n))
	return sum


def isPrime(n): #Check if a given number is a prime
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

if __name__ == "__main__":
	while True:
		print ("\nWhat would you like to do?")
		print ("1. Check if a number is a Smith number: ")
		print ("2. List all the Smith Numbers up to a number you choose: ")
		print ("0. To quit")
		option = int(input("\nPlease choose: "))
		if option == 1 or option == 2 or option == 0:
			break
	if option == 1:
		n = input("Enter a number to check: \n")
		SmithTest(int(n))
	if option == 2:
		n = input("List all the Smith Number up until: \n")
		for i in range(3, n):
			SmithTest(i)
