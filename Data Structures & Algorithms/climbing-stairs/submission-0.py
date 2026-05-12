class Solution:
    def climbStairs(self, n: int) -> int:
        # n = target number
        # add 1 or 2 tell value = n
        # find all possible distinct ways you can add 1 or 2 to reach n

        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs((n-1)) + self.climbStairs((n-2))