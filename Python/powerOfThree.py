"""
https://leetcode.com/problems/power-of-three/
Difficulty: Easy

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.


Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true

Constraints:
-2^31 <= n <= 2^31 - 1
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            while n % 3 == 0:   # remainder = 0, n is multiples of 3
                n /= 3    # continue to divide n by 3
            if n == 1:    # if n last value is 1, when n is cubic rooted, it returns int
                return True
            return False
