class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        
        for ind, n in enumerate(nums):
            for k in num_set.keys():
                if n+k == target:
                    return [num_set[k], ind]

            if n not in num_set.keys():
                num_set[n] = ind
            