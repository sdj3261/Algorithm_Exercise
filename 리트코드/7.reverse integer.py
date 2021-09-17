class Solution:
    def reverse(self, x: int) -> int:
        sentinel = '2147483648' if x < 0 else '2147483647'

        sign = -1 if x < 0 else 1
        s = str(x)[::-1].rstrip('-')
        no_overflow = s.rjust(len(sentinel), '0') < sentinel

        return int(s) * sign * no_overflow