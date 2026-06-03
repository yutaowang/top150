class Solution:
    def isValid(self, s: str) -> bool:
        st=[]; mp={')':'(',']':'[','}':'{'}
        for c in s:
            if c in mp.values(): st.append(c)
            elif not st or st.pop()!=mp[c]: return False
        return not st
