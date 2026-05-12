class Solution:
    def recHelper(self, nums: List[int], l: int, r:int, target: int) -> int:
        print("l: " + str(l) + ' r: ' + str(r))

        p = (int)((r-l)/2) + l
        print('p: ' + str(p))

        if target == nums[p]:
            return p
        
        if (l+1) == r or l >= r:
            if target == nums[r]:
                return r
            return -1

        if target < nums[p]:
            # target is left of p
            return self.recHelper(nums, l, p, target)

        if target > nums[p]:
            # target is right of p
            return self.recHelper(nums, p, r, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.recHelper(nums, 0, (len(nums) - 1), target)
        

    

        