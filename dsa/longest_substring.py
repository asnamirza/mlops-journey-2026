def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    """
    char_set = set()          # stores characters in current window
    left = 0                   # left pointer of the window
    max_len = 0                 # result

    for right in range(len(s)):           # right pointer moves through the string
        # If s[right] is a duplicate, shrink window from left until it's gone
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Add the new character and update max length
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

# Example test
if __name__ == "__main__":
    test = "abcabcbb"
    print(length_of_longest_substring(test))  # Output: 3