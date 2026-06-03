from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []; i = 0
        while i < len(words):
            j = i; line_len = 0
            while j < len(words) and line_len + len(words[j]) + (j-i) <= maxWidth:
                line_len += len(words[j]); j += 1
            gaps = j - i - 1
            if j == len(words) or gaps == 0:
                line = ' '.join(words[i:j]).ljust(maxWidth)
            else:
                spaces = maxWidth - line_len; each, extra = divmod(spaces, gaps)
                line = ''.join(words[k] + ' ' * (each + (k-i < extra)) for k in range(i, j-1)) + words[j-1]
            res.append(line); i = j
        return res
