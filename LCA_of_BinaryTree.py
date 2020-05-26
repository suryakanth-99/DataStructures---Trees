class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, value, q):
    if node is None:
        node = Node(value)
        q.append(node)
        return node
    temp = q[0]
    if temp.left is None:
        temp.left = insert(temp.left, value, q)
    elif temp.right is None:
        temp.right = insert(temp.right, value, q)
        q.pop(0)
    return node


def printlevelorder(node):

    queue = []
    if node is None:
        return
    queue.append(node)
    while len(queue) > 0:
        print(queue[0].data, end=' ')
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def findlca(node, val1, val2):
    if node is None:
        return node
    if node.data == val1 or node.data == val2:
        return node
    left_lca = findlca(node.left, val1, val2)
    right_lca = findlca(node.right, val1, val2)
    if left_lca and right_lca:
        return node
    return left_lca if left_lca is not None else right_lca


if __name__ == '__main__':
    root = None
    arr = [int(i) for i in input().split()]
    q = []
    for i in range(len(arr)):
        root = insert(root, arr[i], q)
    printlevelorder(root)
    least_lca = findlca(root, 4, 5)
    print()
    print(least_lca.data)
