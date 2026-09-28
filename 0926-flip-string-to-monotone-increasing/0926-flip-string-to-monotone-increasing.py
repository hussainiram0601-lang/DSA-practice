class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = {(len(s),True):0,(len(s),False):0}
        def dfs(i,mono):
            if (i,mono) in dp:
                return dp[(i,mono)]
            if mono and s[i]=='0':
                dp[(i,mono)]=min(1+dfs(i+1,mono=False),dfs(i+1,mono))

            elif mono and s[i]=='1':
                dp[(i, mono)]= min(1+dfs(i+1,mono),dfs(i+1,mono=False))
            elif not mono and s[i]=='1':
                dp[(i, mono)]= dfs(i+1,mono)
            else:
                dp[(i,mono)]=1+dfs(i+1,mono)
            return dp[(i, mono)]
        return dfs(0,True)