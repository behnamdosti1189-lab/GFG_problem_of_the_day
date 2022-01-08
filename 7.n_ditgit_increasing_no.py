'''
N Digit numbers with digits in increasing order 

Given an integer N, print all the N digit numbers in increasing order, such that their digits are in strictly increasing order(from left to right).

Input:
N = 2
Output:
12 13 14 15 16 17 18 19 23....79 89
Explanation:
For N = 2, the correct sequence is
12 13 14 15 16 17 18 19 23 and so on 
up to 89.


https://practice.geeksforgeeks.org/problems/n-digit-numbers-with-digits-in-increasing-order5903/1#
'''
# Python3 program to prall n-digit numbers
# whose digits are str1ictly increasing
# from left to right

# Function to prall n-digit numbers
# whose digits are str1ictly increasing
# from left to right.
# out --> Stores current output
#		 number as str1ing
# start --> Current starting digit
#		 to be considered
def findStrictlyIncreasingNum(start, out, n):
	
	# If number becomes N-digit, print
	if (n == 0):
		print(out, end = " ")
		return

	# start from (prev digit + 1) till 9
	for i in range(start, 10):
		
		# append current digit to number
		str1 = out + str(i)

		# recurse for next digit
		findStrictlyIncreasingNum(i + 1,
							str1, n - 1)

# Driver code
n = 3
findStrictlyIncreasingNum(0, "", n)

# This code is contributed by Mohit Kumar
