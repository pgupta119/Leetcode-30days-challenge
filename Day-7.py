# iven an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

#time complexity is O(n*n)

# New solution usinh hashmap (dictionary)

class Solution:
    def twoSum(self, nums : List[int], target: int ):
        hashmap = {}
        for i in range(i,len(nums)):
            c = target - nums[i]
            if c in hashmap:
                return [i, hashmap[c]]
            hashmap[nums[i]] = i

y = Solution
# target = 9 , nums = [2,7,11,15]
print(y.twoSum([2,7,11,15], 9))

