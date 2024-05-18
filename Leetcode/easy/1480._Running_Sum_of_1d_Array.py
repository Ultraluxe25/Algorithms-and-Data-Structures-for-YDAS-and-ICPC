"""
1480. Running Sum of 1d Array

Easy

Hint
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 
Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

# Solution 1 (Old version)
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums[:i]) for i in range(1, len(nums) + 1)]
    

# Solution 2 (18.05.2024)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(len(nums)):
            new_nums.append(sum(nums[:i + 1]))

        return new_nums
        

# Solution 3 (better in 18.05.2024)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_nums = []
        total = 0 
        
        for i in range(len(nums)):
            total += nums[i]
            new_nums.append(total)

        return new_nums
        