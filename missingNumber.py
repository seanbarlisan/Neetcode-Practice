def missingNumber(nums):
        missing = 0
        counter = 0
        for x in nums:
            if x == counter: # something is wrong
                print(nums[x])
                x += 1
            else:
                missing = x
        return missing

if __name__ == "__main__":
    nums = [1, 2, 3]
    x = missingNumber(nums)
    print(x)