## 剑指 Offer 40. 最小的k个数
>链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

### 思路一：排序
对数组按小到大排序，然后获取前k个值
排序最快的快排，时间复杂度为 O(log n)
#### 代码实现
```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        return arr[:k]
```

### 思路二：大顶堆
- 维护一个大小为k的大顶堆，遍历数组arr，把前k个值直接插入大顶堆
- 从第k+1个值开始，比较与堆顶元素的大小
- 如果比堆顶元素大，则跳过
- 如果比堆顶元素小，则加入堆中
- 遍历arr后，得到的大顶堆就是前k个最小的结果

#### 代码实现
由于Python 语言中的对为小根堆，所以需要对数组中所有的数取其相反数，才能使用小根堆维护前 k 小值。
```python
import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0 : return []
        leng = len(arr)
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k,leng):
            heapq.heappushpop(hp, -arr[i])
        return [-x for x in hp]
```

### 思路三：快排切分
注意找前 K 大/前 K 小问题不需要对整个数组进行 O(NlogN)O(NlogN) 的排序！
例如本题，直接通过快排切分排好第 K 小的数（下标为 K-1），那么它左边的数就是比它小的另外 K-1 个数啦～
下面代码给出了详细的注释，没啥好啰嗦的，就是快排模版要记牢
```java
class Solution {
    public int[] getLeastNumbers(int[] arr, int k) {
        if (k == 0 || arr.length == 0) {
            return new int[0];
        }
        // 最后一个参数表示我们要找的是下标为k-1的数
        return quickSearch(arr, 0, arr.length - 1, k - 1);
    }

    private int[] quickSearch(int[] nums, int lo, int hi, int k) {
        // 每快排切分1次，找到排序后下标为j的元素，如果j恰好等于k就返回j以及j左边所有的数；
        int j = partition(nums, lo, hi);
        if (j == k) {
            return Arrays.copyOf(nums, j + 1);
        }
        // 否则根据下标j与k的大小关系来决定继续切分左段还是右段。
        return j > k? quickSearch(nums, lo, j - 1, k): quickSearch(nums, j + 1, hi, k);
    }

    // 快排切分，返回下标j，使得比nums[j]小的数都在j的左边，比nums[j]大的数都在j的右边。
    private int partition(int[] nums, int lo, int hi) {
        int v = nums[lo];
        int i = lo, j = hi + 1;
        while (true) {
            while (++i <= hi && nums[i] < v);
            while (--j >= lo && nums[j] > v);
            if (i >= j) {
                break;
            }
            int t = nums[j];
            nums[j] = nums[i];
            nums[i] = t;
        }
        nums[lo] = nums[j];
        nums[j] = v;
        return j;
    }
}
```
快排切分时间复杂度分析： 因为我们是要找下标为k的元素，第一次切分的时候需要遍历整个数组 (0 ~ n) 找到了下标是 j 的元素，假如 k 比 j 小的话，那么我们下次切分只要遍历数组 (0~k-1)的元素就行啦，反之如果 k 比 j 大的话，那下次切分只要遍历数组 (k+1～n) 的元素就行啦，总之可以看作每次调用 partition 遍历的元素数目都是上一次遍历的 1/2，因此时间复杂度是 N + N/2 + N/4 + ... + N/N = 2N, 因此时间复杂度是 O(N)O(N)。


