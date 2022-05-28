# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#Solution

class Solution:
    def climbStairs(self, n: int) -> int:
        last, s_last = 1, 1
        for i in range(n - 1):
            temp = last
            last = last + s_last
            s_last = temp

        return last