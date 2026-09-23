# Sum of Squares
# Given an integer n, calculate the sum of squares of all integers from 1 to n.

# Example 1:
# Input: n = 6
# Output: 91
# Explanation: 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 = 1 + 4 + 9 + 16 + 25 + 36 = 91

# Example 2:
# Input: n = 3
# Output: 14
# Explanation: 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

# Example 3:
# Input: n = 1
# Output: 1
# Explanation: 1^2 = 1

# Examples
# Example 1:
# Input: {"n": 6}
# Output: 91
# Explanation: Sample testcase example

# Example 2:
# Input: {"n": 3}
# Output: 14
# Explanation: Sample testcase example

# Example 3:
# Input: {"n": 1}
# Output: 1
# Explanation: Sample testcase example

# Example 4:
# Input: {"n": 5}
# Output: 55
# Explanation: Sample testcase example

# Constraints:
# Time limit: 2000 ms
# Memory limit: 256 MB

def sumOfSquares(n):
    total = 0

    for i in range(1, n + 1):
        total += i ** 2

    return total

print(sumOfSquares(9))