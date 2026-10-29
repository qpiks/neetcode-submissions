class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        p1, p2, ans = 0, 0, 0
        for i in range(len(s)):
            if s[i] in seen:
                new_p1 = seen[s[i]] + 1
                for x in s[p1:new_p1]:
                    seen.pop(x) 
                p1 = new_p1
            ans = max(ans, p2 - p1 + 1)
            p2 += 1
            seen[s[i]] = i
        return ans

                

        