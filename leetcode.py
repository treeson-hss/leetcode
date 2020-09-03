
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


if __name__ == '__main__':
    list_str = [6, 7, 5, 2, 4, 5, 9, 3]
    largestRectangleArea(list_str)
