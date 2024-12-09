class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # creates a dictionary but prevents the key error
        for s in strs: # iterate through the string list 
            count = [0] * 26 # creates different character counts for 26 letters
            for c in s: # iterate through the character in each string
                count[ord(c) - ord('a')] += 1 # ASCII difference for each character
            res[tuple(count)].append(s) # store in result, where we store an immutable string comma separated list of char counts, appending based on string KEY to value COUNT
        return res.values() # return the res.values of all groups