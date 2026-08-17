class Solution:
    def partitionString(self, s: str) -> int:
        curstring = set()
        res = 1
        for c in s:
            if c in curstring:
                res+=1
                curstring= set()
            curstring.add(c)
        return res