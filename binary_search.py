class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 # sets the variables for left and right to do BST

        while left <= right: # while loop to continue while 0 < right most number index
            mid = (left + right) // 2 # add the two to get to get middle index
            if nums[mid] == target: # if the element equals target
                return mid # return
            elif mid < target: # if not
                left = mid + 1 # go through right side and continue
            else: # otherwise 
                right = mid - 1 # go through left side and continue
        return -1
        
        