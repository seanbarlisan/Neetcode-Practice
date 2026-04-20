def missingNumber(nums):
    num_set = set(nums) # create a set of the nums values
    n = len(nums) # length of the nums list
    for i in range(n+1): # for range of n
        if i not in num_set: # if value is not in that set
            return i # return it

if __name__ == "__main__":
    nums = [0, 1, 3]
    x = missingNumber(nums)
    print(x)