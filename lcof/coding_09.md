## 剑指 Offer 09. 用两个栈实现队列
>链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
```shell
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
```
示例 2：
```shell
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
```
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

### 思路一：delete时维护
定义两个stack，一个做输入栈一个做输出栈，在append时直接往输入栈添加，delete时首先判断输出栈是否为空，是则把输入栈的所有元素都移动到输出栈

#### 代码实现
```python
class CQueue:

    def __init__(self):
        self.push = []
        self.pop  = []

    def appendTail(self, value: int) -> None:
        self.push.append(value)

    def deleteHead(self) -> int:
        if not self.pop :
            while self.push:
                self.pop.append(self.push.pop())
        return self.pop.pop() if self.pop else -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

### 复杂度分析
- 时间复杂度：对于插入和删除操作，时间复杂度均为 O(1)。插入不多说，对于删除操作，虽然看起来是 O(n) 的时间复杂度，但是仔细考虑下每个元素只会「至多被插入和弹出 stack2 一次」，因此均摊下来每个元素被删除的时间复杂度仍为 O(1)。

空间复杂度：O(n)。需要使用两个栈存储已有的元素。


### 思路二：push时维护(速度极慢，不推荐)
上面是只在delete时维护，其实也可以在push时维护，也需要两个栈，但是一个是输入输出栈，另一个是临时存储栈。
在有新元素插入时，首先把输入输出栈的所有元素移动到临时栈，再把新元素插入输入输出栈，这样后入的元素就存储在栈底，然后再把所有元素从临时栈取出。
#### 代码实现
```python
class CQueue:

    def __init__(self):
        self.data = []
        self.cache  = []

    def appendTail(self, value: int) -> None:
        while self.data:
            self.cache.append(self.data.pop())
        self.data.append(value)
        while self.cache:
            self.data.append(self.cache.pop())

    def deleteHead(self) -> int:
        return self.data.pop() if self.data else -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```





