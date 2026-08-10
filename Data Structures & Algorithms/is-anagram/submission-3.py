class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = {}
        for x in s:
            if not letters.get(x):
                letters.update({x: 1})
            else:
                letters[x] = letters[x] + 1
        for x in t:
            if not letters.get(x):
                return False
            else:
                letters[x] = letters[x] - 1 
        for x in letters.values():
            if x != 0:
                return False
        return True
        
        


        