# Functions to analysis values in a list

# print the numbers in the list
def printNums(numbers):
	for num in numbers:
		print(num)

# sum the values in the list
def sumNums(numbers):
	total=0
	for num in numbers:
		total += num
	return total

# returns the mean average of a list of numbers
def averageNums(numbers):
	sumOfNums = sumNums(numbers)
	average = sumOfNums / len(numbers)
	return average

# returns the variance of a list of numbers
def varianceNums(numbers):
	variance = [0]*len(numbers)
	average = averageNums(numbers)
	for index,num in enumerate(numbers):
		variance[index]=(num-average)**2
	return averageNums(variance)

# returns the standard dev. of a list of numbers
def stdDevNums(numbers):
	variance = varianceNums(numbers)
	try: 
		return variance ** .5
	except TypeError:
		print("wrong data type received")

