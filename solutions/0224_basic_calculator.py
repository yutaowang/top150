class Solution:
    def calculate(self, s: str) -> int:
        ans=num=0; sign=1; st=[]
        for c in s:
            if c.isdigit(): num=num*10+int(c)
            elif c in '+-':
                ans += sign*num; num=0; sign=1 if c=='+' else -1
            elif c=='(': st.append((ans,sign)); ans=0; sign=1
            elif c==')':
                ans += sign*num; num=0; prev,psign=st.pop(); ans=prev+psign*ans
        return ans + sign*num
