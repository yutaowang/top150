from typing import List
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        w=len(words[0]); total=w*len(words); need=Counter(words); res=[]
        for offset in range(w):
            l=offset; have=Counter(); count=0
            for r in range(offset, len(s)-w+1, w):
                word=s[r:r+w]
                if word in need:
                    have[word]+=1; count+=1
                    while have[word]>need[word]:
                        have[s[l:l+w]]-=1; count-=1; l+=w
                    if count==len(words): res.append(l)
                else:
                    have.clear(); count=0; l=r+w
        return res
