class Solution:

    def strtoInt(self, str: str) -> int:

        str = str.strip()
        if not str: return 0
        res, i, sign = 0, 1, 1

        # boundry
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 2
        if str[0] == "-":
            sign = -1
        elif str[0] != "+":
            i = 0

        for c in str[i:]:
            if not "0" <= c <= "9": break

            if res > bndry or res == bndry and c > "7":
                return int_max if sign == 1 else int_min

            # updata
            res = res * 10 + ord(c) - ord("0")

        return res
