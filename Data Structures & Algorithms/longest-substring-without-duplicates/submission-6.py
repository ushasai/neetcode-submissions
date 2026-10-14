class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        seen = set()
        left = 0
        length = 0
        p1 = 0
        for i in range(p1, len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            length = max(length, len(seen))
        return length



        