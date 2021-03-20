from typing import List


class Solution:

    def __init__(self):
        self.res = 0

    def isStraight(self, nums:List[int]) -> bool:
        """抽取牌面是否为顺子"""

        # 设置初始条件
        repeat = set()
        mi, ma = 0, 14

        for num in nums:
            if num == 0: continue
            mi = min(num, mi)
            ma = max(num, ma)
            # 判断重复
            if num in repeat: return False
            repeat.add(num)

        return ma - mi < 5

    def sumNums(self, n: int) -> int:
        """ｎ数据累加"""

        # 递归
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res

    def strToInt(self, str:str) -> int:

        # 去除空格
        str = str.strip()
        # 设置初始值
        res, i, sign = 0, 1, 1
        # 边界条件
        mi_int, ma_int, bndry = -2**31, 2**31, 2**31//10
        if str[0] == "-": sign = -1
        elif str[0] != "+": i = 0  # 无符号整数
        # 遍历字符串
        for c in str[i:]:
            if not "0" <= c <= "9": break
            # 越界判断
            if res > bndry or res == bndry and c > "7":return ma_int if sign == 1 else ma_int
            # 更新
            res = res*10 + ord(c) - ord("0")

        return sign*res
