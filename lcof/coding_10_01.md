## 剑指 Offer 10- I. 斐波那契数列
>链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：1

示例 2：
输入：n = 5
输出：5
 

提示：
0 <= n <= 100
注意：本题与主站 509 题相同：https://leetcode-cn.com/problems/fibonacci-number/

### 这道题和../array/70题的做法基本是一样的，只是初始值即前面两个数的值不同，并且按题目要求最后结果需要取模，这里新增一个lru_cache的解法

### lrucache
```python
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n<2:
            return n
        return (self.fib(n-1)+self.fib(n-2))%1000000007
```


