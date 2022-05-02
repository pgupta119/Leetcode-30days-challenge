# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
#
# class Solution:
#     def isHappy(self, n: int) -> bool:


def happy_number(n):
    n = str(n) # convert into string
    if int(n) == 1:  # if n equals 1 then return true
        return True
      elif int(n) >7: # if n greater than 7 the use recursion ( I am not able to think what would be stop condition)
          j = 0
          for i in range(0,len(str(n))):  # each digit take one at a time
              j = j + int(n[i]) * int(n[i]) #  get the square and sum with next digit square
          n = j # assign new n
          return happy_number(n) # recursion
      else:
          return False  # if value below 6 ( I checked for 2 to  6  it is not happy number
      return n

# My approach is not because it doesn't know where I have to and for large number it will exceed the time

#leet code solution
def isHappy(self, n: int) -> bool:

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1

x = isHappy()
print(x.isHappy(19))


