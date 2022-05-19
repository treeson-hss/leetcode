package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

//记录三种遍历的非递归实现
// 前序遍历
func preorder(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	result := make([]int, 0)
	stack := make([]*TreeNode, 0)
	for root != nil || len(stack) != 0 {
		for root != nil {
			result = append(result, root.Val)
			stack = append(stack, root)
			root = root.Left
		}
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		root = node.Right
	}
	return result

}

// 中序遍历
func inorder(root *TreeNode) []int {
	result := make([]int, 0)
	stack := make([]*TreeNode, 0)
	for len(stack) != 0 || root != nil {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, node.Val)
		root = node.Right
	}
	return result
}

// 后序遍历
func postorder(root *TreeNode) []int {
	result := make([]int, 0)
	stack := make([]*TreeNode, 0)
	var lastVisited *TreeNode
	for len(stack) != 0 || root != nil {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		// 这里先看看，先不弹出
		node := stack[len(stack)-1]
		// 根节点必须在右节点弹出之后，再弹出
		if node.Right == nil || node.Right == lastVisited {
			stack = stack[:len(stack)-1]
			result = append(result, node.Val)
			// 标记当前这个节点已经弹出过
			lastVisited = node
		} else {
			root = node.Right
		}

	}
	return result
}

func main() {
	fmt.Println("")
}
