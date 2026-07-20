class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for ch in list(s):
            if ch!="#":
                s1.append(ch)
            elif len(s1)>0:
                s1.pop()
        for ch in list(t):
            if ch!="#":
                s2.append(ch)
            elif len(s2)>0:
                s2.pop()   
        return s1 == s2