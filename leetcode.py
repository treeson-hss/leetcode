
def evalRPN(tokens) -> int:
    num_list = []
    for element in num_list:
        print("append")
        if element not in ['+', '-', '/', '*']:
            num_list.append(element)

            continue
        num_1 = num_list.pop()
        num_2 = num_list.pop()
        if element in '+':
            num_list.append(num_2 + num_1)
        elif element in '-':
            num_list.append(num_2 - num_1)
        elif element in '*':
            num_list.append(num_2 * num_1)
        elif element in '/':
            num_list.append(int(num_2 / num_1))
        else:
            num_list.append(element)

    return num_list.pop()


def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return
    j = 0
    for index in range(0, len(nums)):
        if nums[index] != 0:
            nums[j] = nums[index]
            if index > j:
                nums[index] = 0
            print(index, j, nums)
            j += 1


def threeSum(nums):
    leng = len(nums)
    if not nums or leng < 3:
        return []
    nums.sort()
    if nums[0] > 0:
        return []
    res = []
    for i in range(leng):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        left = i + 1
        right = leng - 1
        while left < right:
            print(i, left, right)
            target = nums[i] + nums[left] + nums[right]
            if target == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif target < 0:
                left += 1
            else:
                right -= 1
    return res


def largestRectangleArea(heights) -> int:
    size = len(heights)
    res = 0
    heights = [0] + heights + [0]
    # 先放入哨兵结点，在循环中就不用做非空判断
    stack = [0]
    size += 2
    print(heights)

    for i in range(1, size):
        print(i, res, stack[-1])
        while heights[i] < heights[stack[-1]]:
            cur_height = heights[stack.pop()]
            cur_width = i - stack[-1] - 1
            res = max(res, cur_height * cur_width)
        stack.append(i)
    print(stack)
    return res


def generateParenthesis(n: int):
    if n == 0:
        return []
    total_l = []
    total_l.append([None])    # 0组括号时记为None
    total_l.append(["()"])    # 1组括号只有一种情况
    for i in range(2, n+1):    # 开始计算i组括号时的括号组合
        l = []
        for j in range(i):    # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
            now_list1 = total_l[j]    # p = j 时的括号组合情况
            now_list2 = total_l[i-1-j]    # q = (i-1) - j 时的括号组合情况
            for k1 in now_list1:
                for k2 in now_list2:
                    print(f'i:{i}, j:{j}, k1:{k1}, k2:{k2}')
                    if k1 == None:
                        k1 = ""
                    if k2 == None:
                        k2 = ""
                    el = "(" + k1 + ")" + k2
                    print(f'el:{el}')
                    l.append(el)    # 把所有可能的情况添加到 l 中
        total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
    return total_l[n]


if __name__ == '__main__':
    # list_str = [6, 7, 5, 2, 4, 5, 9, 3]
    # largestRectangleArea(list_str)
    generateParenthesis(6)
