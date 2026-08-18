class Solution:
    def isPalindrome(self, s: str) -> bool:
        for l in s:
            if not l.isalnum():
                s = s.replace(l, "")
        s = s.lower()

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:

                print (s[i], i, s[len(s) - i - 1], len(s) - i - 1)
                return False
        return True



        