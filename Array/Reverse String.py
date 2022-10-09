# Link - https://leetcode.com/problems/reverse-string/
# Author - Tarek Hossain
# Input: s = ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]

def reverseString(s):
    start = 0
    end = len(s)-1

    def reverse(s, start, end):
        if start >= end:
            return
        s[start], s[end] = s[end], s[start]
        reverse(s, start + 1, end - 1)
    reverse(s, start, end)
    return s


s = ["h", "e", "l", "l", "o"]
rev = reverseString(s)
print(rev)