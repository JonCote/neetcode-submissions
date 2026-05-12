class Solution:
    def recHelper(self, nums: List[int], l: int, r:int, target: int) -> int:
        if l > r:
            return -1
        
        print("l: " + str(l) + ' r: ' + str(r))

        p = (int)((r-l)/2) + l
        print('p: ' + str(p))

        if target == nums[p]:
            return p

        if target < nums[p]:
            # target is left of p
            if p == r:
                p -= 1
            return self.recHelper(nums, l, p, target)

        if target > nums[p]:
            # target is right of p
            if p == l:
                p += 1
            return self.recHelper(nums, p, r, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.recHelper(nums, 0, (len(nums) - 1), target)
        

    

        