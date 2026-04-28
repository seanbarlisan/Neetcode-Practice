def climbStairs(n):

    def dfs(i):
        if i >= n:
            return i == n 
        return dfs(i+1) + dfs(i+2)

    return dfs(0)


if __name__ == "__main__":

    n = 3
    result = climbStairs(n)
    print(result)
    