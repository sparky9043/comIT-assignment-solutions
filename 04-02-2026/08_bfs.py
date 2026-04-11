"""
    Breadth-First Search Implementation
    
    Given a binary tree, return its level order traversal.
    The input should be the root node and the output should be a list of
    lists of integers, with the "i"th list containing the values of nodes
    on level i, from left to right
"""

# deque is used for a very efficient way to add/remove items

# Each Node consists of the following:
# 1. value is for the node's value itself
# 2. left is for the left lower level
# 3. right is for the right lower level
from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return str(self.value)

def level_order_traversal(root: Node) -> list[list[int]]:
    # collect final result here in result:
    result = []
    
    # A queue will be made for collecting level results one at a time
    queue: list[Node] = [root]
    
    # This will keep running until the queue is completely empty
    while len(queue) > 0:
        n = len(queue)
        
        # This will connect values of each Node
        new_level = []
        
        for _ in range(n):
            # Pop the first index of the queue (leftmost value)
            current_node = queue.pop(0)
            
            # The popped result is now saved as a value in new_level
            new_level.append(current_node)
            
            # For each child that exists, append it into the queue
            for child in [current_node.left, current_node.right]:
                if child is not None:
                    queue.append(child)
                    
        # Append the list of all values in the new_level into result
        result.append(new_level)

    # Return final result
    return result

# Flood Fill Implementation
def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]):
    num_rows, num_cols = len(image), len(image[0])
    
    def get_neighbors(coord, color):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                if image[neighbor_row][neighbor_col] == color:
                    yield neighbor_row, neighbor_col
    
    def bfs(root):
        queue = deque([root])
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        r, c = root
        color = image[r][c]
        image[r][c] = replacement
        visited[r][c] = True
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node, color):
                r, c = neighbor
                if visited[r][c]:
                    continue
                image[r][c] = replacement
                queue.append(neighbor)
                visited[r][c] = True
    bfs((r, c))
    return image
            
if __name__ == "__main__":
    # Breadth-First Tree Printing:
    print("=" * 50)
    print("Print Level by Level")
    print("       8")
    print("     /   \\")
    print("    3     10")
    print("   / \\      \\")
    print("  1   6      14")
    print("     / \\     /")
    print("    4   7   13")
    root1 = Node(8)
    root1.left = Node(3)
    root1.right = Node(10)
    root1.left.left = Node(1)
    root1.left.right = Node(6)
    root1.left.right.left = Node(4)
    root1.left.right.right = Node(7)
    root1.right.right = Node(14)
    root1.right.left = Node(9)
    root1.right.right.left = Node(13)
    print(level_order_traversal(root1))
    print("=" * 50)
    print("Flood Fill")
    image = [
        [1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    new_image = flood_fill(2, 1, 9, image)
    for row in new_image:
        print(row)
    print("replaced 0s with 9s")