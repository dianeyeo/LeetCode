"""
https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}

        stack = []
        for n in s:
            if n in pairs:
                stack.append(n)
            else:
                if not stack:
                    return False
                valid = stack.pop()
                if pairs[valid] != n:
                    return False
        return False if stack else True

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[]{}"))
