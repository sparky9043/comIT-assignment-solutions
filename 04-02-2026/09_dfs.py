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

# Number of Islands
def count_number_of_islands(grid: list[list[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    def get_neighbors(coord):
        res = []
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))
        return res
    
    def dfs(coord):
        r, c = coord
        if grid[r][c] == 0:
            return
        grid[r][c] = 0
        for neighbor in get_neighbors(coord):
            nr, nc = neighbor
            if grid[nr][nc] == 1:
                dfs(neighbor)
    
    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 1:
                dfs((r, c))
                count += 1
    return count

if __name__ == "__main__":
    print("=" * 50)
    print("Max Depth Problem")
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
    print("=" * 50)
    print("Number of Islands")
    grid = [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 1, 1, 1],
    ]
    for row in grid:
        print(row)
        
    print("How many islands?", count_number_of_islands(grid))