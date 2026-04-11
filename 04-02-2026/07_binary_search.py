# Binary Search Implementation

# Find the first True in a Sorted Boolean Array
def find_boundary(arr: list[bool]) -> int:
    # Start with first and last index as left and right
    left, right = 0, len(arr) - 1
    
    # Start with -1 as boundary index
    boundary_index = -1
    
    # While loop triggers for as long as left index <= right
    while left <= right:
        mid = (left + right) // 2
        
        # If the middle element is True, cut the right side, move middle to left
        if arr[mid]:
            boundary_index = mid
            right = mid - 1

        # If the middle element is False, cut left, move middle to right
        else:
            left = mid + 1
            
        # The above will cause falses to be eliminated until from the left
        # and cause the trues to close in on the right side until you get the
        # first true
    
    return boundary_index

# Find the Minimum in Rotated Sorted Array
def find_min_rotated(arr: list[int]) -> int:
    # The only thing this is doing is making sure that we convert
    # the list into monotonic booleans like the above
    # Example: [30, 40, 50, 10, 20]
    # Let's say we ask, are these elements <= the last element (<= 20)?
    # this converts it to [False, False, False, True, True] -> Monotonic!
    left, right = 0, len(arr) - 1
    boundary_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return boundary_index
    
if __name__ == "__main__":
    boolean_list = [False, False, False, False, False, True, True]
    numbers = [30, 40, 50, 60, 10]
    print("=" * 80)
    print("Find the index of the first True in a list of booleans", end="\n")
    print()
    print("List of booleans:", boolean_list)
    print("Location of first True:", find_boundary(boolean_list))
    print()
    print("=" * 80)
    print("Find the index of the smallest number in a rotated array", end="\n\n")
    print("List of numbers:", numbers)
    print("Location of smallest number:", find_min_rotated(numbers))
