class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        words = {}
        for i in range(len(strs)):
            w = "".join(sorted(strs[i]))
            if words.get(w) != None:
                res[words[w]].append(strs[i])
            else: 
                words.update({w: len(res)})
                res.append([strs[i]])
        return res


        