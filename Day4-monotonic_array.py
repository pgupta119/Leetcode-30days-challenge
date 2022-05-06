# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.


#My Solution
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        count_i = 0
        count_d = 0
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count_i = 1 + count_i
            elif nums[i] == nums[i + 1]:
                count_i = 1 + count_i
                count_d = 1 + count_d
            else:
                count_d = 1 + count_d
        if (nums[len(nums) - 2]) < (nums[len(nums) - 1]):
            count_i = count_i + 1
        elif (nums[len(nums) - 2]) > (nums[len(nums) - 1]):
            count_d = count_d + 1
        else:
            count_i = 1 + count_i
            count_d = 1 + count_d
        if (count_i == len(nums)) | (count_d == len(nums)):
            return True
        else:
            return False



#actual solution: One pass
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(0, len(A) - 1):
            if A[i] > A[i + 1]:
                increasing = False
            if A[i] < A[i + 1]:
                decreasing = False

        return increasing or decreasing



