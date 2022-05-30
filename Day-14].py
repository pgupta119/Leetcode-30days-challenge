#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

#SOlution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(num) -1
        while start <= end :
            mid = start + (end -start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid -1
            else:
                start = mid+1
        return -1