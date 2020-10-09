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


if __name__ == "__main__":
    for i in range(10, 200, 1):
        arr = np.random.permutation(i)
        # bubble = bubblesort(arr.copy())
        # print(bubble)
        #insert = insertsort(arr.copy())
        # print(insert)
        select = selectsort(arr.copy())
        print(select)
        # print(arr)
