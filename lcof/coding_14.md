## 剑指 Offer 14- I. 剪绳子
>链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]* k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

### 思路一：暴力破解
把求解 F(n)F(n) 的问题分解成求解 F(n-1)F(n−1) 的问题，以此类推，直到求解到 F(2)F(2) 时，F(2) = 1F(2)=1，递推回去，问题就得到了解决。这用到的就是分治的思想。

分治思想的解决方法往往是递归，注意到我们每次将一段绳子剪成两段时，剩下的部分可以继续剪，也可以不剪， 因此我们得到了递归函数 F(n)=max(i×(n−i),i×F(n−i)),i=1,2,...,n−2。

#### 代码
```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 2:
            return 1
        res = n-1
        for i in range(1, n):
            res = max(res, i * (n -i) , i * self.cuttingRope(n -i))
        return res
```
显然会超时
#### 复杂度分析
- 时间复杂度：O(2^N^)
- 空间复杂度：O(2^N^)

### 记忆化搜索
上面超时是因为在递归状态树中，有很多重复的计算，同样可以使用缓存来记录已经计算过的节点，这里增加一个 lrucache的
```python
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def cuttingRope(self, n: int) -> int:
        if n <= 2:
            return 1
        res = n-1
        for i in range(1, n):
            res = max(res, i * (n -i) , i * self.cuttingRope(n -i))
        return res
```

#### 复杂度分析
- 时间复杂度：O(n), 由于加了缓存，所以每个状态子节点都只会访问一次
- 空间复杂度：O(n)，递归占用空间以及lrucache占用

### 动态规划
上面是自顶向下的递归做法，同样可以转成自顶向上的动态规划
- 重复子问题：每根木棍第一次折断的时候，有n-1种折法，折断后的棍子，还可以选择继续折，或者不折，取决于两者的最大值
- 中间状态：opt[i]，i表示木棍长度
- dp方程：opt[i] = max(opt[i], j * (i - j), j * opt[i - j]), j = 1...i-1

#### 代码
```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        opt = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i):
                opt[i] = max(opt[i], j * (i - j) , j * opt[i-j])
        return opt[n]
```
#### 复杂度分析
- 时间复杂度：O(n^2^)
- 空间复杂度：O(n)

### 思路四：动态规划 优化
我们发现任何大于 3 的数都可以拆分为数字 1，2，3 的和，且它们对 3 的余数总是 0，1，2，因此我们可以仅用 dp[0]，dp[1]，dp[2] 表示所有大于 3 的值，这样空间复杂度可降到 O(1)。






