#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.(at least one positive number)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        current_max = 0
        for i in range(0, len(nums)):
            max_sum = max_sum + nums[i]
            if max_sum < 0:
                max_sum = 0
            if max_sum > current_max:
                current_max = max_sum
        return current_max



y = Solution
print(y.maxSubArray([[-2,1,-3,4,-1,2,1,-5,4])