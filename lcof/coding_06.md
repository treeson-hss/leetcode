## 剑指 Offer 06. 从尾到头打印链表
>链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
 
限制：
0 <= 链表长度 <= 10000

### 注意
在编写代码前，要跟面试官沟通清楚，根据面试官提出的不同性能需求（时间效率优先 or 空间效率优先 or 不允许改变链表结构 or 云云），给出不同的算法。

### 思路一：反转数组
遍历链表，把每个值添加到list，再把list反转
#### 代码实现
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        root,res = head,[]
        while root:
            res.append(root.val)
            root = root.next
        return res[::-1]
```
#### 复杂度分析
- 时间复杂度：O(n)
- 空间复杂度：O(n)


### 思路二：栈+数组 (也可用递归)
上面的反转数组，可以通过遍历链表的时候，首先入栈，遍历完之后依次出栈即可代替反转
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:return []
        return self.reversePrint(head.next) + [head.val]
```
#### 复杂度分析
- 时间复杂度：O(n)
- 空间复杂度：O(n)

用递归的话，虽然简洁，但是如果链表过长，函数调用的层级就会很深，从而可能导致函数栈溢出


### 思路三：遍历 + 数组
先遍历链表，得到链表长度，再从数组的最后添加链表的值
#### 代码实现
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        leng, root = 0, head
        while root:
            leng += 1
            root = root.next 
        res = [0] * leng
        while head:
            res[leng-1] = head.val
            head, leng = head.next, leng - 1
        return res
        
```

### 思路四：反转链表
把链表反转，再遍历添加到数组中
#### 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:return []
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        res = []
        while pre:
            res.append(pre.val)
            pre = pre.next
        return res
```


