## 剑指 Offer 05. 替换空格
> https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

限制：
0 <= s 的长度 <= 10000

### 注意
c++和ruby等少数语言的string是可变的，可以使用原地算法，即先计算出替换后的长度，从后往前遍历并替换元素，这样每个元素就只需要移动一次
但是对于python、go和Java等大部分语言，string都是不可变的，只能是新建一个数据结构来解决

### 思路一：库函数
#### 代码实现
```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")
```

### 思路二：字符数组
新建一个数组，长度为字符串长度
遍历每个字符，如果不是空格，则直接添加到数组，如果是空格，则分别添加 % 2 0三个字符到数组，最后数组转成字符串

#### 代码实现
```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        char = [''] * len(s)
        for ch in s:
            if ch != ' ':
                char.append(ch)
            else:
                char.append('%20')
        return ''.join(char)
```
#### 复杂度分析：
时间复杂度 O(N) ： 遍历使用 O(N) ，每轮添加（修改）字符操作使用 O(1) ；
空间复杂度 O(N) ： 新建的 list 使用了线性大小的额外空间。




