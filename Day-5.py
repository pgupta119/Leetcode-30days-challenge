# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# My solution
class Solution:
    def containsDuplicate(nums: List[int]):
        count = 0
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums [j]:
                    count = count +1
        if count > 0 :
            return True
        else:
            return False

# Problem with this solution is to Time complexity O(N*N)


# Better approach is to find length of the distinct number length and compare with actual length of the list



class Solution:
    def containsDuplicate(nums: List[int]):
        return True if len(set(nums)) < len(nums) else False


y = Solution
print(y.containsDuplicate([3,4,5,6,6,9]))


