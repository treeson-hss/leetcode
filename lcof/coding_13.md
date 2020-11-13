## 剑指 Offer 13. 机器人的运动范围
>链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1]。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20

### 思路一：dfs
这道题实际上是在一个二维数组上，会有一些障碍物，问机器人能走多少个格子。不能简单的直接减去有障碍物的格子，因为如果障碍物把空格子之间隔开了的话，机器人也是无法到达剩余的空格子的。所以，在四连通方向中，如果每个方向都走不下去，说明是走完了可用的格子了，直接返回。
这里统计的是能走多少个格子，所以统计肯定是不能有重复的，题中说了，机器人是可以沿着上下左右四个方向走的。但你想一下，任何一个格子你从任何一个方向进来（比如从上面进来），那么他只能往其他3个方向走，因为如果在往回走就重复了。但实际上我们只要沿着两个方向走就可以了，一个是右边，一个是下边

#### 代码
```python
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k == 0:return 1
        direct = [(0,1),(1,0)]
        visited = set()
        def dfs(x, y):
            if self.count_index(x) + self.count_index(y) > k:return 
            visited.add((x,y))
            for r,c in direct:
                n_i, n_j = x+r, y+c
                if 0<=n_i<m and 0<= n_j < n and (n_i, n_j) not in visited:
                    dfs(n_i, n_j)
        dfs(0, 0)
        return len(visited)

    def count_index(self, index):
        ten = index // 10
        one = index % 10
        return ten + one
```
#### 复杂度分析

时间复杂度：O(mn)，其中 m 为方格的行数，n 为方格的列数。考虑所有格子都能进入，那么搜索的时候一个格子最多会被访问的次数为常数，所以时间复杂度为 O(2mn)=O(mn)。

空间复杂度：O(mn)，其中 m 为方格的行数，n 为方格的列数。搜索的时候需要一个大小为 O(mn) 的标记结构用来标记每个格子是否被走过。


### 思路二：bfs
和dfs类似，bfs是没有下一层格子可以遍历时表明已经走完了

#### 代码
```python
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k == 0:return 1
        direct = [(0,1),(1,0),(-1,0),(0,-1)]
        visited, queue = set(), [(0,0)]
        while queue:
            x, y = queue.pop()
            if self.count_index(x) + self.count_index(y) > k:continue
            visited.add((x,y))
            level = []
            for r,c in direct:
                n_i, n_j = x+r, y+c
                if 0<=n_i<m and 0<= n_j < n and (n_i, n_j) not in visited:
                    level.append((n_i,n_j))
            queue.extend(level)
        return len(visited)

    def count_index(self, index):
        ten = index // 10
        one = index % 10
        return ten + one

```
#### 复杂度分析

时间复杂度：O(mn)，其中 m 为方格的行数，n 为方格的列数。考虑所有格子都能进入，那么搜索的时候一个格子最多会被访问的次数为常数，所以时间复杂度为 O(2mn)=O(mn)。

空间复杂度：O(mn)，其中 m 为方格的行数，n 为方格的列数。搜索的时候需要一个大小为 O(mn) 的标记结构用来标记每个格子是否被走过。









