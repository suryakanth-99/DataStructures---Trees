class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def CreateBST(root , value):
    if root is None:
        return Node(value)
    if value<root.data:
        root.left=CreateBST(root.left,value)
    if value>root.data :
        root.right=CreateBST(root.right,value)
    return root


def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)


def leftview(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) != 0:
        i=0
        size = len(queue)
        while(i < size):
            i+=1
            temp = queue.pop()
            if i == 1:
                print(temp.data, end=' ')
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)


if __name__ == '__main__':
    root = None
    n=int(input())
    arr=[int(i) for i in input().split()]
    for i in range(n):
        root=CreateBST(root,arr[i])
    #printInorder(root)
    leftview(root)