class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        pair = [[scores[i],ages[i]]  for i in range(len(scores))]
        pair.sort()
        dp = [pair[i][0] for i in range(len(pair))]
        for i in range(len(pair)):
            Mscore, Mage = pair[i]
            for j in range(i):
                score, age = pair[j]
                if Mage>= age:
                    dp[i]= max( dp[i], dp[j]+Mscore )
        return max(dp)
        