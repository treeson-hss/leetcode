## 剑指 Offer 11. 旋转数组的最小数字
>链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof


把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：
输入：[3,4,5,1,2]
输出：1

示例 2：
输入：[2,2,2,0,1]
输出：0
**注意**: 本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/


如果没有重复元素，这道题应该跟../array/153题一样。。。
### 思路一：遍历
遍历数组，找到第一个递减的元素，就是最小值
#### 代码
```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        last = float('-inf')
        for num in numbers:
            if num < last:return num
            last = num
        return numbers[0]
```
### 思路二：二分查找
考虑数组中的最后一个元素 x：在最小值右侧的元素，它们的值一定都小于等于 x；而在最小值左侧的元素，它们的值一定都大于等于 x。因此，我们可以根据这一条性质，通过二分查找的方法找出最小值。

在153题的基础上，可以得出中值和右值大小的两种情况，大于或小于，但是在有重复元素的情况下，会出现等于的情况，如果等于的话，就不能确定最小值到底是在左边还是在右边。
中值等于右值==n的情况：
- 如果最小值刚好是n，那就只需保留中值，中值往右的都可以忽略
- 如果最小值位于中值的左边，说明只需保留中值，中值往右的也都可以忽略
- 如果最小值位于中值的右边，那可以收缩左边界，但是由于还有上面两种情况，我们不能明确最小值的位置，所以不能盲目收缩左边界；但是，在这种情况下，最小值到右值是单调递增的，所以如果我们能把右值向左移一位，就会重新变成 中值 > 右值的情况，也就可以收缩左边界了
- 综上，为了能包含以上三种情况，最佳办法就是右值往左取一位。

#### 代码
```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1
        return numbers[left]
```
#### 复杂度分析
- 时间复杂度：平均时间复杂度为O(logn)，其中 n 是数组 numbers 的长度。如果数组是随机生成的，那么数组中包含相同元素的概率很低，在二分查找的过程中，大部分情况都会忽略一半的区间。而在最坏情况下，如果数组中的元素完全相同，那么 while 循环就需要执行 n 次，每次忽略区间的右端点，时间复杂度为O(n)。

- 空间复杂度：O(1)。













