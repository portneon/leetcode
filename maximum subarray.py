# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:


nums = [-1,-2]
max_sum = float('-inf')
current_sum = 0
for ele in nums:
    current_sum = max(ele, current_sum + ele)
    max_sum = max(max_sum, current_sum)
print(max_sum)

