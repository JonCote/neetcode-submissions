class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            if n in num_dict.keys():
                return [num_dict[n], i]
        
            if (target - n) not in num_dict.keys(): 
                num_dict[target - n] = i

        return [0, 0]

        