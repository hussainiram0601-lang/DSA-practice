class Solution:
    def sortString(self, s):
        l1= list(s)
        l1.sort()
        return "".join(l1)
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in s:
            key = self.sortString(i)
            if key in dict1:
                dict1[key].append(i)
            else:
                dict1[key] = [i]
        return list(dict1.values())
             