import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        req = math.floor(len(nums) / 2)
        counts = {}
        
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

            if counts[n] > req:
                return n

        return -1