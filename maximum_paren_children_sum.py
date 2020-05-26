class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def CreateBinaryTree(node, value, q):
    if node is None:
        node = Node(value)
        q.append(node)
        return node
    temp = q[0]
    if temp.left is None:
        temp.left = CreateBinaryTree(temp.left, value, q)
    elif temp.right is None:
        temp.right = CreateBinaryTree(temp.right, value, q)
        q.pop(0)
    return node


def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)

def parent_child_sum(root):
    if root is None:
        return 0
    if root.left is None or root.right is None:
        return 0
    else:
        result = root.data + root.left.data + root.right.data
    return max(result, parent_child_sum(root.left), parent_child_sum(root.right))


if __name__ == '__main__':
    root=None
    q=[]
    arr=[int(i) for i in input().split()]
    for i in range(len(arr)):
        root=CreateBinaryTree(root, arr[i], q)
    printInorder(root)
    print()
    print(parent_child_sum(root))