class Solution:
    def convert(self, s: str, numRows: int) -> str:
        str_zzak = ""
        str_hole = ""
        answer = ""
        interval = (numRows - 1) * 2
        step = (numRows - index) * 2
        if len(s) == 1:
            return s
        if numRows == 2:
            for i in range(len(s)):
                if i == 0 or i % 2 == 0:
            str_zzak.append(s[i])
            else:
            str_hole.append(s[i])
            return str_zzak + str_hole
        else:



