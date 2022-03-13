"""
https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(nums) == 1:
            return False        # list contain only 1 element, no duplicates
        
        nums.sort()        # sort list
        while len(nums) > 1:
            for i in range(len(nums)):
                if nums[i] == nums[i-1]:        # if current element is equal to previous element
                    return True
            return False
