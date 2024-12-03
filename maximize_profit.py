def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # initialize the two array indexes
        maxP = 0 # initialize the initial profit with 0

        while r < len(prices): # while we are less than length of prices
            if prices[l] < prices[r]: # if previous price better than the next day
                profit = prices[r] - prices[l] # find profit
                maxP = max(maxP, profit) # max function to compare both
            else:
                l = r # update value
            r += l # update value
        return maxP # return