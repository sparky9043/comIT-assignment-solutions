# Priority Queue Implementation
# Find the k closets points to the origin
from heapq import heappop, heappush


def k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    heap: list[tuple[int, list[int]]] = []
    
    for pt in points:
        heappush(heap, (pt[0] ** 2 + pt[1] ** 2, pt))
        
    result = []
    for _ in range(k):
        _, pt = heappop(heap)
        result.append(pt)
    
    return result

if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    print("Priority Queue/Heap Implementation:")
    print("Points:")
    for point in points:
        print(point)
        
    print("Find k = 2 closets points")
    print(k_closest_points(points, 2))