from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words=set(wordDict); dp=[False]*(len(s)+1); dp[0]=True
        for i in range(1,len(s)+1): dp[i]=any(dp[j] and s[j:i] in words for j in range(i))
        return dp[-1]
