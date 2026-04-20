def missingNumber(nums):
    num_set = set(nums)
    n = len(nums)
    for i in range(n+1):
        if i not in num_set:
            return i

if __name__ == "__main__":
    nums = [0, 1, 3]
    x = missingNumber(nums)
    print(x)