class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        seen = {}
        seen1 = {}
        l = 0

        for ch in t:
            seen[ch] = seen.get(ch, 0) + 1

        have, need = 0, len(seen)
        ansl, ansr = -1, -1
        anslen = float('inf')

        for i in range(len(s)):
            ch = s[i]
            seen1[ch] = seen1.get(ch, 0) + 1
            

            if ch in seen and seen1[ch] == seen[ch]:
                have += 1

            while have == need: 
                if i - l + 1 < anslen:
                    ansl, ansr = l, i
                    anslen = i - l + 1
                if seen1.get(s[l], 0) <= seen.get(s[l], -1):
                    have -= 1
                seen1[s[l]] -= 1
                l += 1

        if anslen != float('inf'):
            return s[ansl : ansr + 1]
        return ""


            

        

        