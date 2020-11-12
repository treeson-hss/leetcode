## 剑指 Offer 12. 矩阵中的路径
>链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
```shell
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
```
但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

示例 1：
```shell
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
```
示例 2：
```shell
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
```
提示：
1 <= board.length <= 200
1 <= board[i].length <= 200
注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/

### 思路一：回溯
- 定义一个四连通图方向数组，作为路径前进方向
- 遍历每个元素，通过上面的方向数组得到下一个元素，同时把当前元素做标记，表示已经访问过，防止再次访问，然后与目标字符串做比对，如果不符，则撤销当前状态，回溯到上一级
- 遍历的时候可以直接比较第一个元素，不符则直接跳过
- 使用四连通方向时注意边界，防止数组越界
- 需要做一些剪枝，如把当前要匹配的Word的位置也做参数传入，直接比较该字符，不等则直接减掉

#### 代码实现
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direct = [(-1, 0), (0,-1), (1,0), (0,1)]
        row, col, self.res = len(board), len(board[0]), False
        def backtrack(x, y, index):# index 表示当前需要匹配Word的第几个字符
            if board[x][y] != word[index]:return 
            if index >= len(word) - 1:
                self.res = True
                return
            tmp = board[x][y]
            board[x][y] = '-'
            for r,c in direct:
                new_i, new_j = x+r,y+c
                if not self.res and 0 <= new_i < row and 0 <= new_j < col and board[new_i][new_j] != '-' :
                    backtrack(new_i, new_j, index+1)
            board[x][y] = tmp
        for i in range(0, row):
            for j in range(0, col):
                if self.res:
                    return True
                backtrack(i,j, 0)
        return self.res
```





