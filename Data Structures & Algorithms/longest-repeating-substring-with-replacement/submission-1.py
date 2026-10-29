class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        ans = 0
        l = 0
        for i in range(len(s)):
            ch = s[i]
            chars[ch] = chars.get(ch, 0) + 1
            while i - l + 1 - max(chars.values()) > k:
                chars[s[l]] -= 1 
                l += 1
            ans = max(ans, i - l + 1)
        return ans

