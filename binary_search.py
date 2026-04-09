class Solution:
    def search(self, nums: List[int], target: int) -> int: # lower bound solution to cover everything 
        l, r = 0, len(nums) # left = 0, right is equal to the length of the nums array

        while l < r: # while left is less than right
            m = l + ((r - l) // 2) # midpoint calculation
            if nums[m] > target: # if this is greater than the target
                r = m # we set right value to the mid point 
            elif nums[m] <= target:
                l = m + 1 # decrease lower bound 
        return l - 1 if (l and nums[l - 1] == target) else -1 # return this function?
        
        