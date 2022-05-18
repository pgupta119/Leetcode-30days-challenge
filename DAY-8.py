# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return nums1.intersection(nums2)


y.Solution
print(y.intersection([1,2,4,4,9,6],[2,3,4,5,6,7,2]))

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return  list(nums1 & nums2)