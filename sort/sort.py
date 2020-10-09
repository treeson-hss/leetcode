#! env python3
# coding:utf-8
import numpy as np
import random

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


if __name__ == "__main__":
    for i in range(10, 110, 1):
        arr = np.random.permutation(i)
        # bubble = bubblesort(arr.copy())
        # print(bubble)
        # insert = insertsort(arr.copy())
        # print(insert)
        # select = selectsort(arr.copy())
        # print(select)
        merge = mergesort(arr.copy())
        print(merge)
        # print(arr)
