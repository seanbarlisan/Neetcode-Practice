def isPalindrome(self, s: str) -> bool:
        newStr = '' # Create a new string 
        for c in s: # For character in string
            if c.isalnum(): # if valid character
                newStr += c.lower() # append into new string 
        return newStr == newStr[::-1] # compare two strings and return bool 