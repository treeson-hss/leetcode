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

### 思路五：数学推导 （贪心）
切分规则：
- 最优： 3 。把绳子尽可能切为多个长度为 3 的片段，留下的最后一段绳子的长度可能为 0,1,2 三种情况。
- 次优： 2 。若最后一段绳子长度为 2 ；则保留，不再拆为 1+1 。
- 最差： 1 。若最后一段绳子长度为 1 ；则应把一份 3 + 1 替换为 2+2，因为2×2>3×1。
算法流程：
- 当 n≤3 时，按照规则应不切分，但由于题目要求必须剪成 m>1 段，因此必须剪出一段长度为 1 的绳子，即返回 n - 1 。
- 当 n>3 时，求 n 除以 3 的 整数部分 a 和 余数部分 b （即 n = 3a + b），并分为以下三种情况：
    - 当 b = 0 时，直接返回 3^a^；
    - 当 b = 1 时，要将一个 1 + 3 转换为 2+2，因此返回 3^a-1^ * 4；
    - 当 b = 2 时，返回 3^a^ ×2。

>为什么切分为3的优先级最高 可以利用均值不等式求出乘积最大值 L(m)=(n/m)^m 对此式求导（可利用对数法），可以证明当 m=n/e 时，乘积取最大，此时每段绳子的长度为 n/(n/e)=e，自然对数e的值为2.718，显然接近3，所以总体来讲3最好

>也可以从另外一个角度证明：当n >=5 时，可以证明 2(n-2) > n, 3(n-3) > n，也就是说当绳子的长度大于或等于5时，把它剪成2段或者3段是最好的；且由于当n>=5时，3(n-3) > 2(n-2)，所以3是最优的

#### 复杂度分析：
- 时间复杂度 O(1) ： 仅有求整、求余、次方运算。
- 空间复杂度 O(1) ： 变量 a 和 b 使用常数大小额外空间。
>幂运算：查阅资料，提到浮点取幂为 O(1) 。
求整和求余运算：资料提到不超过机器数的整数可以看作是 O(1) ；
Python 中常见有三种幂计算函数： * 和 pow() 的时间复杂度均为 O(log a) ；而 math.pow() 始终调用 C 库的 pow() 函数，其执行浮点取幂，时间复杂度为 O(1)。

#### 代码
```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

```




