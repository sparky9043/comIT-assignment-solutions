# DFS Template; Recursion Solution
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.value)

# Basic DFS Implementation
def dfs(root, target):
    if root is None:
        return None
    
    if root.value == target:
        return root
    
    left = dfs(root.left, target)
    
    if left is not None:
        return left

    return dfs(root.right, target)

# Given the root of a binary tree, return its maximum depth
def tree_max_depth(root: Node) -> int:
    def dfs(root):
        if not root:
            return 0
        return max(dfs(root.left), dfs(root.right)) + 1
    
    return dfs(root) - 1 if root else 0

# Use bfs to show all levels:
def level_order_traversal(root: Node) -> list[list[int]]:
    result = []
    queue: list[Node] = [root]

    while len(queue) > 0:
        n = len(queue)
        new_level = []
        
        for _ in range(n):
            current_node = queue.pop(0)
            new_level.append(current_node)
            for child in [current_node.left, current_node.right]:
                if child is not None:
                    queue.append(child)
        result.append(new_level)
    return result

if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right = Node(14)
    root.right.right.right = Node(18)
    root.right.right.left = Node(13)
    print('Print nodes in each level using BFS first')
    print('Tree Levels:', level_order_traversal(root))
    print('Max Depth:', tree_max_depth(root))