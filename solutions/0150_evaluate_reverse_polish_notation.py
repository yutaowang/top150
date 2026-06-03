from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for t in tokens:
            if t not in '+-*/': st.append(int(t)); continue
            b,a=st.pop(),st.pop()
            st.append(a+b if t=='+' else a-b if t=='-' else a*b if t=='*' else int(a/b))
        return st[-1]
