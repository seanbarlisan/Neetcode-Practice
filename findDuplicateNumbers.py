def duplicateNumbers(nums):
    seen = set()
    n = 0
    for x in nums:
        if x in seen:
            n = x
        else:
            seen.add(x)

    return n

if __name__ == "__main__":

    nums = [1, 2, 3, 4, 2]
    n = duplicateNumbers(nums)
    print(n)