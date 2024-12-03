def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same length
        if len(s) != len(t):
            return False

        char_count_s = {} # Initalize the two char_count arrays
        char_count_t = {}

        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1 # Increments char count, use get to make sure that there is a key and index
        for char in t:
            char_count_t[char] = char_count_t.get(char,0) + 1

        return char_count_s == char_count_t # Compare the values