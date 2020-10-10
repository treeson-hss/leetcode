#! env python3
# coding:utf-8
import numpy as np
import random
import time

# 冒泡排序


def bubblesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n):
        break_flag = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                break_flag = True
        if not break_flag:
            break
    return arr


# 插入排序
"""
左边有序右边未排序
"""


def insertsort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n-1):
        current = arr[i+1]  # 未排序列表中需要比较的数
        sortes_index = i
        while sortes_index >= 0 and current < arr[sortes_index]:
            arr[sortes_index+1] = arr[sortes_index]
            sortes_index -= 1
        arr[sortes_index+1] = current
    return arr

# 选择排序


def selectsort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 归并排序


def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = int(n / 2)

    def merge(left, right):
        res, l_n, r_n = [], len(left), len(right)
        i = j = 0
        for _ in range(l_n+r_n):
            if i >= l_n:
                res.append(right[j])
                j += 1
            elif j >= r_n:
                res.append(left[i])
                i += 1
            elif left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        return res

    return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))

# 快速排序


"""
end：arr的最后一个元素下标
"""


def quicksort(arr, start, end):
    n = len(arr)
    if n <= 1 or start >= end or start < 0 or end >= n:
        return arr

    def partition(arr, start, end):
        if start >= end:
            return end
        p = random.randint(start, end)
        sorted_i = start
        arr[end], arr[p] = arr[p], arr[end]
        for j in range(start, end):
            if arr[j] < arr[end]:
                arr[sorted_i], arr[j] = arr[j], arr[sorted_i]
                sorted_i += 1
        arr[sorted_i], arr[end] = arr[end], arr[sorted_i]
        return sorted_i
    p = partition(arr, start, end)
    quicksort(arr, start, p - 1)
    quicksort(arr, p + 1, end)
    return arr


if __name__ == "__main__":
    for i in range(10, 110, 1):
        arr = np.random.permutation(i)
        pre_bubble = time.time()
        bubble = bubblesort(arr.copy())
        # print(bubble)
        post_bubble = time.time()
        insert = insertsort(arr.copy())
        post_insert = time.time()
        # print(insert)
        select = selectsort(arr.copy())
        post_select = time.time()
        # print(select)
        merge = mergesort(arr.copy())
        post_merge = time.time()
        # print(merge)
        quick = quicksort(arr.copy(), 0, len(arr) - 1)
        post_quick = time.time()
        print(
            f"bubble:{post_bubble-pre_bubble}, insert:{post_insert-post_bubble}, select:{post_select-post_insert}, merge:{post_merge-post_select}, quick:{post_quick-post_merge}")
        # print(quick)
        # print(arr)
