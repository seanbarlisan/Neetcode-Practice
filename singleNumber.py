def singleNumber(nums):
    seen = set()
    numsRange = range(len(nums))
    single = 0
    for x in numsRange:
        if nums[x] in seen:
            single = nums[x]
            seen.add(nums[x])
        else:
            single = nums[x]
    return single

if __name__== "__main__":
    numsList = [1, 2, 3, 4, 2, 1]
    result = singleNumber(numsList)
    print(result)