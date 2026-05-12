class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3

        for n in nums:
            if n == 0:
                count[0] += 1
            if n == 1:
                count[1] += 1
            if n == 2:
                count[2] += 1
        
        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1

        
        