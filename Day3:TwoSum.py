# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,3], target = 6
# Output: [0,1]

# My Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = [] # store the index of the sum
        for i in range(0, len(nums)): # loop for number one by one
            for j in range(i + 1, len(nums)): # loop for check each number to each other
                if nums[i] + nums[j] == target: #sum found
                    a.append(i) # add the index to the list
                    a.append(j) # add the index to the list

        return a
# Time complexity of the code is 0(n*2)
# Better Solution using hash table

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # create a  dictionary which store the index and  corresponding value
        for i in range(len(nums)): #  check for each value
            complement = target - nums[i]  # get the number which need to add to the current so get the target value
            if complement in hashmap: # check the  number in the dictionary if it is present or not
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
