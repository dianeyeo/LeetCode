"""
https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:  # if empty str, return ""
            return ""
        prefix = ""
        strs = sorted(strs)     # sort strs based on length
        for n in strs[0]:
             if strs[-1].startswith(prefix+n):  # retrieves each str if str starts with same letter as first str
                prefix += n
             else:
                break
        return prefix
