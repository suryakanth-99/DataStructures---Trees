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

def leafsum(root,ans):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return ans+root.data
    return leafsum(root.left,ans) + leafsum(root.right,ans)


if __name__ == '__main__':
    root=None
    n=int(input())
    arr=[int(i) for i in input().split()]
    for i in range(n):
        root=CreateBST(root,arr[i])

    print(leafsum(root,0))