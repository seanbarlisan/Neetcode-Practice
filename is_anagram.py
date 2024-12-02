def is_anagram(s, t):
    # Anagrams must have the same length
    if len(s) != len(t):
        return False

    # Create a frequency dictionary
    char_count = {}

    # Increment count for `s`, decrement for `t`
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in t:
        char_count[char] = char_count.get(char, 0) - 1

    # Check if all counts are zero
    return all(count == 0 for count in char_count.values())

# Example Usage:
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))   # Output: False
