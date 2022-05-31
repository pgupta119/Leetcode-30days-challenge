# Let's call an array arr a mountain if the following properties hold:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].


#my solution

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i, j= 0, len(arr)-1
        while i <j:
            if arr[i] < arr[i+1]:
                i =i+1
            if arr[j] < arr[j-1]:
                j = j-1
        return i

#second solution

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # i, j= 0, len(arr)-1
        # while i <j:
        #     if arr[i] < arr[i+1]:
        #         i =i+1
        #     if arr[j] < arr[j-1]:
        #         j = j-1
        # return i
        left, right = 0, len(arr) -1
        while left < right:
            mid = left + (right -left)//2
            if arr[mid] < arr[mid + 1]:
                left = mid +1
            else:
                right = mid
        return left