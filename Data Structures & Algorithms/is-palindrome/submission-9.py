class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            char = char.lower()
            if char.isalnum():
                new_str += char
        return new_str == new_str[::-1]
            