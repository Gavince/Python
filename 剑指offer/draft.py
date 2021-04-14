import collections
from typing import List


class Solution:
    """字符串习题"""

    def finfdRepeatNumber(self, nums):
        """找寻重复数字"""

        i = 1
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        return -1

    def constrcuctArr(self, a):
        """构建数组乘积"""

        # 临时变量
        b, tmp = [1] * len(a), 1
        # 计算下三角
        for i in range(1, len(a)):
            b[i] = a[i - 1] * b[i - 1]
        # 计算上三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp

        return b

    def isMatch(self, s: str, p: str) -> bool:
        """正则表达式匹配"""

        if not p: return not s
        first_match = bool(s and p[0] in {".", s[0]})
        if len(p) >= 2 and p[1] == ".":
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def firstUniqueChar(self, s: str) -> bool:
        """找寻字符流中第一个不重复的字符"""

        dic = {}
        for c in s:
            #  重复出现为False
            dic[c] = not c in dic

        for k, v in dic.items():
            if dic[v]: return k

        return " "

    def maxSlideWindow(self, nums, k):
        """滑动窗口最大值"""

        deque = collections.deque()
        res, n = [], len(nums)
        # 有效遍历
        for i, j in zip(range(1 - k, n - k + 1), range(n)):
            # 左删除
            if i > 0 and deque[0] == nums[i - 1]: return deque.popleft()
            # 右添加(存储有可能成为最大值的元素)
            while deque and deque[-1] < nums[j]: deque.pop()
            deque.append(nums[j])
            # 滑动窗口移动保存数值
            if i >= 0:
                res.append(deque[0])
        return res

    def myPow(self, x: float, n: float) -> float:
        """自定义整数次方"""

        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            # 奇数和偶数的区别
            if n & 1: res *= x
            x *= x
            n >>= 1

        return res

    def spiralOrder(self, matrix):
        """顺时针打印矩阵"""

        if not matrix: return []
        res = []
        # 边界条件
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while True:
            # 从左向右
            for i in range(l, r + 1): res.append(matrix[t][i])
            t += 1
            if t > b: break
            # 从上向下
            for i in range(t, b + 1): res.append(matrix[i][r])
            r -= 1
            if r < l: break
            # 从右向左
            for i in range(r, l - 1, -1): res.append(matrix[b][i])
            b -= 1
            if b < t: break
            # 从下向上
            for i in range(b, t - 1, -1): res.append(matrix[i][l])
            l += 1
            if l > r: break

        return res

    def permutation(self, s: str):
        """字符串的排列"""

        c, res = list(s), []

        def dfs(x):
            """固定位置，寻找排列组合"""
            # 递归终点返回数值
            if x == len(c) - 1:
                res.append("".join(c))
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x + 1)
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return res

    def quickSort(self, nums, strat, end):
        """快速排序法"""

        if strat >= end: return
        # 设置基准
        mid = nums[strat]
        low, hight = strat, end
        while low < hight:
            while low < hight and nums[low] < mid: low += 1
            while low < hight and nums[hight] >= mid: hight -= 1
            nums[low], nums[hight] = nums[hight], nums[low]

        # 交换基准m
        nums[low] = mid
        # 左遍历
        self.quickSort(nums, strat, low - 1)
        # 右遍历
        self.quickSort(nums, low + 1, end)

    def minNumber(self, nums):
        """数组元素拼接最小值"""

        def quick(l, r):
            if l >= r:
                return
            low, hight = l, r
            while low < hight:
                while low < hight and strs[low] + strs[l] < strs[l] + strs[low]: low += 1
                while low < hight and strs[hight] + strs[l] >= strs[l] + strs[hight]: hight -= 1
                strs[low], strs[hight] = strs[hight], strs[low]

            strs[low], strs[l] = strs[l], strs[low]
            quick(l, low - 1)
            quick(low + 1, r)

        # 把整型列表变为字符列表
        strs = [str(c) for c in nums]
        quick(0, len(strs) - 1)
        return "".join(strs)

    def binarySearch(self, nums, target):
        """二分查找:查找指定元素的位置"""
        low = 0
        hight = len(nums) - 1
        while low <= hight:
            mid = (low + hight) // 2
            if target < nums[mid]:
                hight = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid

        return -1

    def search(self, nums, target):
        """给定有序数组，找出重复数字的次数"""

        def helper(tar):
            """查找右边界"""

            low, hight = 0, len(tar) - 1
            while low <= hight:
                mid = (low + hight) // 2
                if nums[mid] <= tar:
                    low = mid + 1
                else:
                    hight = mid - 1

            return low

        return helper(target) - helper(target - 1)

    def findContinuousSequence(self, target):
        """连续数为目标的和"""
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(range(i, j + 1))
            # 左减去
            if s >= target:
                s -= i
                i += 1
            # 右叠加
            else:
                j += 1
                s += j

        return res

    def findContinyousSequence(self, target):
        """连续正整数和为target的序列"""
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(range(i, j + 1))
            # 左删除
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res

    def reverseSelectWords(self, s, n):
        """左旋转前n个字符串"""

        res = []

        for i in range(n, len(s) + n):
            res.append(s[i % len(s)])

        return "".join(res)

    def reverseWords(self, s: str) -> str:
        """翻转单词表法"""

        s = s.strip()
        res = []
        i = j = len(s) - 1
        # 从尾部进行遍历
        while i >= 0:
            while i >= 0 and s[i] != " ": i -= 1
            res.append(s[i + 1:j + 1])
            while s[i] == " ": i -= 1
            j = i
        return "".join(res)

    def isStraigh(self, nums):
        """随机抽取五张牌查看是否为顺子"""

        # 判断重复
        repeat = set()
        mi, ma = 0, 14

        for num in nums:
            if num == 0: continue
            ma = max(ma, num)
            mi = min(mi, num)
            if num in repeat: return False
            repeat.add(num)
        # 满足不重复，最大最小差值小于5
        return ma - mi < 5

    # 1+2+3...n
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:

        n > 1 and self.minNumber(n - 1)
        self.res += n
        return self.res

    def strToInt(self, strs: str) -> int:
        """字符转整数类型"""

        s = strs.strip()
        if not s: return 0
        res, i, sign = 0, 1, 1
        int_max, int_min, bondry = 2 ** 31 - 1, -2 ** 31 - 1, 2 ** 31 // 10

        if s[0] == "-":
            sign = -1
        elif s[0] != "+":
            i = 0
        for c in s[i:]:
            if not "0" <= c <= "9": break
            # 越界处理
            if res > bondry or res == bondry and c > "7": return int_max if sign == 1 else int_min
            # updata
            res = res * 10 + ord(c) - ord(0)

        return res * sign

    def exis(self, board, words: str) -> bool:

        def find(i, j, k):
            """i, j 为坐标 , k为值"""

            # 判断满足条件
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != words[k]: return False
            if len(words) - 1 == k: return True
            # 已访问打标记
            board[i][j] = ""
            res = find(i + 1, j, k + 1) or find(i - 1, j, k + 1) or find(i, j + 1, k + 1) or find(i, j - 1, k + 1)
            # 去除标记（为下次做准备）
            board[i][j] = words[k]
            return res

        for i in range(board):
            for j in range(board[0]):
                if find(i, j, 0): return True

        return False

    def moving(self, m, n, k):

        def dfs(i, j, si, sj):
            # 边界条件
            if i >= m or j >= n or (i, j) in visited:
                return 0
            visited.add((i, j))

            return 1 + \
                   dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + \
                   dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)


class TreeNode:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Tree:
    """树习题"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    def maxDepth(self, root):
        """二叉树的最大深度"""

        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root) -> bool:
        """是否是高度平衡树"""

        def hight(root):
            if root is None: return 0
            leftHight = hight(root.left)
            rightHight = hight(root.right)
            if leftHight == -1 or rightHight == -1 or abs(leftHight - rightHight) > 1:
                return -1
            else:
                return max(leftHight, rightHight) + 1

        return hight(root) >= 0

    def getNextNode(self, pNode):
        """获取结点在z"""

        if pNode.right:
            tmp_node = pNode.next
            while tmp_node.left:
                tmp_node = tmp_node.left
            return tmp_node
        else:
            temp_node = pNode
            while temp_node.next:
                if temp_node.next.left == temp_node:
                    return temp_node
                temp_node = temp_node.next
            return None

    def isSymmetirc(self, root):
        """对称二叉树"""

        def recu(L, R):
            # 退出的两种情况:中间结点不相等或左右一深一浅

            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recu(L.left, R.right) and recu(L.right, R.left)

        return recu(root.left, root.right) if root else None

    def mirror(self, root):
        """二叉树的镜像"""

        if root is None:
            return None

        # 左右互换
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)

    def levelOrder1(self, root):
        """层序遍历"""

        if root is None: return []
        # 使用队列先进后出
        res, deque = [], collections.deque()
        deque.append(root)
        while deque:
            node = deque.popleft()
            res.append(node.val)
            if node.left: deque.append(node.left)
            if node.right: deque.append(node.right)

        return res

    def levelOrder2(self, root):
        """每一次只打印一层数据"""

        if not root: return []
        res, deque = [], collections.deque()
        deque.append(root)

        while deque:
            # 每一层存有一个临时变量
            tmp = []
            for _ in range(len(deque)):
                node = deque.popleft()
                tmp.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(tmp)

        return res

    def levelOrder3(self, root):
        """之字型遍历:奇偶变换, 双端队列，偶头奇尾法"""

        res, deque = [], collections.deque()
        deque.append(root)
        while deque:
            # 双端队列
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2:  # 偶头奇尾法
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))

        return res

    def kthLargest(self, root, k):
        """二叉搜索树的第k个最大值, 中序遍历为有序数组"""

        def dfs(root):
            """层序遍历（右根左）"""
            if root is None: return
            dfs(root.right)
            if self.k == 0: return  # 提前返回
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        # 用于提前返回
        self.k = k
        dfs(root)
        return self.res

    def treeToDoubleList(self, root):
        """二叉搜索树转为双向链表"""

        def dfs(cur):
            """中序遍历"""

            if cur is None: return None
            dfs(cur.left)
            if self.pre:  # 是否存在头结点
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if root is None: return None
        self.pre, self.head = None, None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head  # 首尾相连
        return self.head

    def treeDoubleList(self, root):

        def dfs(cur):

            if cur is None: return None
            dfs(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur

            self.pre = cur
            dfs(cur.right)

        if root is None: return None
        self.pre, self.head = None, None
        dfs(root)
        # 首尾相连
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

    def serialize(self, root):
        """序列化二叉树"""

        pass

    def deserialize(self, root):

        pass

    def maxSubArray(self, nums):
        """最大连续字符串(动态规划，设置)"""

        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)

    def rectCover(self, n):
        """矩形覆盖"""

        # 斐波那契数列
        if n == 0 or n == 1 or n == 2:
            return n

        return self.rectCover(n - 1) + self.rectCover(n - 2)

    def findPath(self, root, expectNumber):
        """和为指定值的二叉树序列(先序遍历)"""

        if root is None:
            return []

        res = []
        #  回朔法条件终点
        if root.val == expectNumber and root.left is None and root.right is None:
            res.append(root.val)

        left = self.findPath(root.left, expectNumber - root.val)
        right = self.findPath(root.right, expectNumber - root.val)

        for path in left + right:
            res.append([root.val] + path)

        return res

    def verifyPostorder(self, postorder):
        """验证一个数组是否为二叉树搜索树的后序遍历"""

        def isTree(postorder):
            root = postorder[-1]
            length = len(postorder)
            # 左子树
            for i in range(length):
                if postorder[i] > root:
                    break
            left = True
            # 右子树
            for j in range(i, length - 1):
                if postorder[j] < root:
                    return False
            right = True
            # 递归子树
            if i > 0:
                left = isTree(postorder[:i])
            if i < length - 1:
                right = isTree(postorder[i:length - 1])

            return left and right

        return isTree(postorder)

    def reConstructBinaryTree(self, pre, tin):
        """重建二叉树"""

        if len(pre) == 0:
            return None
        else:
            # 获取中序遍历中的根结点位置
            r_index = tin.index(pre[0])

        # 构建二叉树
        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:r_index + 1], tin[:r_index])
        root.left = self.reConstructBinaryTree(pre[r_index + 1:], tin[r_index + 1:])

        return root

    def isSubstruct(self, A, B):
        """二叉树的子结构"""

        if not A or not B:
            return False

        return self.include(A, B) or self.include(A.left, B) or self.include(A.right, B)

    def include(self, A, B):

        if not B:
            return True
        if not A or A.val != B.val:
            return False

        return self.include(A.left, B.left) and self.include(A.right, B.right)


#  链表算法
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def findkthToTail(self, pHead, k):
        """双指针法，一前一后"""

        former, latter = pHead, pHead
        for _ in range(len(k)):
            if former is None: return None
            former = former.next

        while former:
            former = former.next
            latter = latter.next

        return latter

    def reverseList(self, pHead):
        """链表的翻转"""

        cur, pre = pHead, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre

    def findFirstCommonNode(self, pHead1, pHead2):
        """烂漫相遇问题（我走过你来时的路）"""

        node1, node2 = pHead1, pHead2
        while node1 != node2:
            node1 = node1.next if node1 else pHead2
            node2 = node2.next if node2 else pHead1
            
        return node1

    def mergeTwoList(self, l1, l2):
        """合并两个有序链表"""

        # 申请新的结点
        cur = dum = TreeNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2

        return dum.next

    def copyRandomList(self, head):
        """复制复杂链表"""

        if head is None:
            return  None

        # 添加附加结点
        cur = head
        while cur:
            tmp = ListNode(0)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next

        # 附加结点随机指针指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 主结点和复附属结点连接
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 对尾结点进行处理
        return res

    def fromTailToHead(self, head):
        """从尾到头打印链表"""
        if head is None:
            return []

        return self.fromTailToHead(head.next) + [head.val]

    def deleteDoubulicates(self, pHead):
        """消除重复结点(不保留重复结点的值)"""

        newhead = TreeNode(0)
        newhead.next = pHead
        pre = newhead
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                tmp = pHead.val
                while pHead and pHead.val == tmp:
                    pHead = pHead.next
            else:
                pre = pre.next
                pHead = pHead.next

        return newhead.next

    def entryNodeOfLoop(self, pHead):
        """链表环入口"""

        if pHead is None:
            return None

        cur = pHead
        stack = []
        while cur:
            if cur not in stack:
                stack.append(cur)
                cur = cur.next
            else:
                return cur

        #  未查找到指定结点
        return None


class SolutionString:

    def lastRemaining(self, n, m):
        """约瑟夫环问题"""

        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i

        return x

    def singleNumber(self, nums):
        """使用异或解决问题"""

        a = 0
        for num in nums:
            a = a^num

        return a

    def fib(self, n):
        """斐波那契数列"""

        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b

        return a%1000000007

    def numWays(self, n):
        """青蛙跳台阶问题，一次一阶台阶或者一次两阶台阶(斐波那契数列变种)"""

        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b

        return a%1000000007

    def numWays2(self, n):
        """一次可以跳台阶不止一阶"""

        if n == 1 or n == 0:
            return n

        return 2*self.numWays2(n - 1)




if __name__ == "__main__":
    obj = Solution()
    print(obj.lastRemaining(3, 1))