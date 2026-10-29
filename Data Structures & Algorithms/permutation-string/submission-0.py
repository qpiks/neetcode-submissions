class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen1, seen2 = {}, {}
        l = 0
        ans = 0
        for ch in s1:
            seen1[ch] = seen1.get(ch, 0) + 1
        for i in range(len(s2)):
            if s2[i] not in seen1:
                seen2 = {}
                l = i + 1
                continue
            seen2[s2[i]] = seen2.get(s2[i], 0) + 1
            while seen2[s2[i]] > seen1[s2[i]]:
                seen2[s2[l]] -= 1
                l += 1
            if seen1 == seen2:
                return True
        return False