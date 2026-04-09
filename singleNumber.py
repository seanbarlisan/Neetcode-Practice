def singleNumber(nums):
    seen = set()
    numsRange = range(len(nums))
    single = 0
    for x in numsRange:
        if nums[x] in seen:
            single = 0
        else:
            seen.add(nums[x])
            single = nums[x]
    return single

if __name__== "__main__":
    numsList = [1, 2, 3, 4, 2, 1]
    result = singleNumber(numsList)
    print(result)