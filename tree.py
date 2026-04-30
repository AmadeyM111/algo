# DFS recursive (Preorder)

def traverse(root):
    if not root:
        return

    #1. process cur node
    print(root.val)

    #2. left subtree
    traverse(root.left)

    #3. right subtree
    traverse(root.right)

# Inorder BFS

def traverse(root):
    if not root:
        return
    
    traverse(root.left)
    print(root.val)
    traverse(root.right)

# Postorder (delete/calculate)

def traverse(root):
    if not root:
        return
    
    traverse(root.left)
    traverse(root.right)
    print(root.val)

# BFS level bypass

from collection import deque

def traverse(root):
    if not root:
        return
    
    q = deque([root])

    while q:
        node = q.popleft()
        print(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def get_layered_representation(root):
    result = []
    DFS(root, 0, result)
    return result

def DFS(node, depth, result):
    if not node:
        return
    # Т.к. мы выбрали preorder, то результат нужно увеличивать
    # не больше, чем на 1
    if depth >= len(result):
        result.append([])
    result[depth].append(node.val)
    DFS(node.left, depth + 1, result)
    DFS(node.right, depth + 1, result)