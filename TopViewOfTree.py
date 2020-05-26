
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelorder(root):
    q=[]
    if root is None:
        return
    q.append(root)
    while(len(q)>0):
        print(q[0].data , end=' ')
        root=q.pop(0)
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)


def CreateBST(root , value):
    if root is None:
        return Node(value)
    if value<root.data:
        root.left=CreateBST(root.left,value)
    if value>root.data :
        root.right=CreateBST(root.right,value)
    return root


def verticalorder(root):
    if root is None:
        return
    mydict = {}
    finaldict = {}
    queue = []
    queue.append(root)
    mydict[root] = 0
    while len(queue) > 0:
        node = queue.pop(0)
        node_level = mydict[node]
        if node_level in finaldict:
            finaldict[node_level].append(node)
        else:
            mylist = []
            mylist.append(node)
            finaldict[node_level] = mylist
        if node.left is not None:
            queue.append(node.left)
            mydict[node.left] = mydict[node] -1
        if node.right is not None:
            queue.append(node.right)
            mydict[node.right] = mydict[node] +1
    for key in sorted(finaldict.keys()):
        node = finaldict[key][0]
        print(node.data, end=' ')


if __name__ == '__main__':
    root = None
    n=int(input())
    arr=[int(i) for i in input().split()]
    for i in range(n):
        root=CreateBST(root,arr[i])
    verticalorder(root)