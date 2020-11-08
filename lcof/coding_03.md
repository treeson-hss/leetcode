## 剑指 Offer 03. 数组中重复的数字
>链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof

找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
 

限制：
2 <= n <= 100000

### 思路一：map + 遍历
遍历数组，用map存储每一个元素，每次判断当前遍历的元素是否在map出现过，是则直接返回
#### 代码实现
```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        cache = {}
        for num in nums:
            if cache.get(num):return num
            cache[num] = 1
        return -1
```
#### 复杂度分析
- 时间复杂度：O(n)。
遍历数组一遍。使用字典，添加元素的时间复杂度为 O(1)，故总的时间复杂度是 O(n)。
- 空间复杂度：O(n)。不重复的每个元素都可能存入字典，因此占用 O(n) 额外空间。

### 思路二：排序
对数组排序，重复数字肯定彼此相邻，返回第一个相邻的元素
#### 代码实现
```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:return nums[i]
        return -1
```
#### 复杂度分析
- 时间复杂度：排序，O(log n)
- 空间复杂度：没有用到额外结构，O(1)


### 思路三：原地排序
- 由于数组元素的值都在指定的范围内，这个范围恰恰好与数组的下标可以一一对应；
- 因此看到数值，就可以知道它应该放在什么位置，这里数字nums[i] 应该放在下标为 i 的位置上，这就像是我们人为编写了哈希函数，这个哈希函数的规则还特别简单；
- 而找到重复的数就是发生了哈希冲突；

分析：这个思路利用到了数组的元素值的范围恰好和数组的长度是一样的，因此数组本身可以当做哈希表来用。遍历一遍就可以找到重复值，但是修改了原始数组。


#### 代码实现
```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i != nums[i]:
                tmp = nums[i]
                if nums[tmp] == tmp:return tmp
                nums[tmp], nums[i] = nums[i], nums[tmp]
        return -1
```
