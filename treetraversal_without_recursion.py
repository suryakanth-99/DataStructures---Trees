class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_without_recursion(node):
    stack=[]
    if node:
        print(node.data)
    while True:
        if node:
            stack.append(node)
            node=node.left
        elif stack:
            node=stack.pop()
            print(node.data,end=' ')
            node=node.right
        else:
            break
    print()


def preorder_without_recursion(node):
    stack=[]
    while True:
        if node:
            print(node.data , end=' ')
            stack.append(node)
            node=node.left
        elif stack:
            node=stack.pop()
            node=node.right
        else:
            break
    print()


if __name__ == '__main__':
    root = None
    min_value = -100
    max_value = 100
    n = int(input())
    l = list(input().rstrip().split())
    i = 0
    treenodes = {}
    while n > 0:
        parent = int(l[i])
        child = int(l[i+1])
        pos = l[i+2]
        if i == 0:
            root = Node(parent)
            treenodes[parent] = root
        parentnode = treenodes[parent]
        childnode = Node(child)
        if pos == 'L':
            parentnode.left = childnode
        else:
            parentnode.right=childnode
        treenodes[child]=childnode

        i=i+3
        n=n-1

    preorder_without_recursion(root)
    inorder_without_recursion(root)