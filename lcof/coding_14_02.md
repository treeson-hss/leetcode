## 剑指 Offer 14- II. 剪绳子 II
>链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
 

提示：

2 <= n <= 1000
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

**这题和 面试题14- I. 剪绳子 主体等价，唯一不同在于本题目涉及 “大数越界情况下的求余问题” 。**
### 思路一：每次计算幂都求余
由于直接计算幂次方会导致溢出，所以每次计算过程都求余，由求余公式：
```shell
(a + b) % p = (a % p + b % p) % p （1）

(a - b) % p = (a % p - b % p ) % p （2）

(a * b) % p = (a % p * b % p) % p （3）
```
先遍历计算出 pow(3,a-1)的值，再根据b的值计算剩下的

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, pow_a = n // 3 - 1, n % 3, 1
        for i in range(0, a):
            pow_a = (pow_a * 3 ) % 1000000007
        if b == 0: return (pow_a * 3)% 1000000007
        if b == 1: return (pow_a * 4)% 1000000007
        return (pow_a * 3 * 2 )% 1000000007
```
#### 复杂度分析
- 时间复杂度：O(n/3),也就是O(n)
- 空间复杂度：只有用到三个变量，为O(1)

### 思路二：快速幂
上面遍历计算pow(3, a-1)的过程，可以通过快速幂来优化
>快速幂：https://blog.csdn.net/qq_19782019/article/details/85621386

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, pow_a, base = n // 3 - 1, n % 3, 1, 3
        # for i in range(0, a):
        #     pow_a = (pow_a * 3 ) % 1000000007
        while a:
            if a % 2 == 0:
                a  = a // 2
                base = (base * base) % 1000000007
            else:
                a = a - 1
                pow_a = pow_a * base
                a = a // 2
                base = (base*base) % 1000000007
                
        if b == 0: return (pow_a * 3)% 1000000007
        if b == 1: return (pow_a * 4)% 1000000007
        return (pow_a * 3 * 2 )% 1000000007
```
简化版
```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, pow_a, base = n // 3 - 1, n % 3, 1, 3
        # for i in range(0, a):
        #     pow_a = (pow_a * 3 ) % 1000000007
        while a:
            if a % 2:
                a  = a - 1
                pow_a = pow_a * base
            a = a // 2
            base = (base*base) % 1000000007
                
        if b == 0: return (pow_a * 3)% 1000000007
        if b == 1: return (pow_a * 4)% 1000000007
        return (pow_a * 3 * 2 )% 1000000007
```

位运算优化：取余可以用 &1 代替， //2可以用 >>1 代替
```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, pow_a, base = n // 3 - 1, n % 3, 1, 3
        # for i in range(0, a):
        #     pow_a = (pow_a * 3 ) % 1000000007
        while a:
            if a & 1:
                a  = a - 1
                pow_a = pow_a * base
            a = a >> 1
            base = (base*base) % 1000000007
                
        if b == 0: return (pow_a * 3)% 1000000007
        if b == 1: return (pow_a * 4)% 1000000007
        return (pow_a * 3 * 2 )% 1000000007
```







