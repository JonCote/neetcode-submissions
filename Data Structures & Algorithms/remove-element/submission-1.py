class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(0, len(nums)):
            if nums[fast] != val:
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                slow += 1

        return slow