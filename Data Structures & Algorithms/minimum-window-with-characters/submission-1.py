class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = s + "A"
        seen = {}
        seen1 = {}
        l = 0

        for ch in t:
            seen[ch] = seen.get(ch, 0) + 1

        have, need = 0, len(seen)

        for i in range(len(s)):
            seen1[s[i]] = seen1.get(s[i], 0) + 1
            

            if s[i] in seen and seen1[s[i]] == seen[s[i]]:
                have += 1

            while have == need: 
                if i - l + 1 < len(ans):
                    ans = s[l : i + 1]
                if seen1.get(s[l], 0) <= seen.get(s[l], -1):
                    have -= 1
                seen1[s[l]] -= 1
                l += 1
        return ans if ans != s + "A" else ""
            

        

        