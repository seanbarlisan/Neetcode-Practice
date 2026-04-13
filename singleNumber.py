def singleNumber(nums):
    seen = set()
    numsRange = range(len(nums))
    for x in numsRange:
        if nums[x] in seen:
            seen.remove(nums[x]) # stack pop 
        else:
            seen.add(nums[x]) # stack insert
    return list(seen)[0]
    

if __name__== "__main__":
    numsList = [4, 1, 2, 1, 2]  
    result = singleNumber(numsList)
    print(result)