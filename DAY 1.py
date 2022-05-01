# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

#solution 1

class Solution:
    def countOdds(low: int, high: int):
        count = 0 # count for odd number
        for i in range(low,high): # checking each number for odd value
            if i%2 !=0 # condition for odd value
                count = count +1 #storing the count of odd number

        return count

# Problem with this solution is time exceed if the number is large

#Solution 2
class Solution:
    def countOdds( low: int, high :int):
        if (low % 2 == 0) & (high % 2 == 0): # when both numbers are even
            count = (high - low) / 2
        elif (low % 2 == 0) & (high % 2 != 0): # when low is even and high is odd
            count = (high - low + 1) / 2
        elif (low % 2 != 0) & (high % 2 == 0): # when low is odd and high is even
            count = ((high - low + 1) / 2)
        else:
            count = (high - low + 2) / 2 # when both are odd

        return int(count)





#Solution from Leet code

    def countOdds(self, low, high):
        return (high + 1) // 2 - low // 2
# the count 1 and low - 1 is low / 2
# the count of odd  numbers between 1 and high is (high + 1) / 2

    #test Cases:
    x = Solution
    print(x.countOdds(low=2,high=3))

