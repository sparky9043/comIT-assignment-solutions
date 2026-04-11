# Sliding Window Implementation

# Fixed Size Sliding Window
# Given a list of non-negative integers, find the largest sum among 
# all sub arrays of length k in nums

def subarray_sum_fixed(nums: list[int], k: int) -> int:
    # First, the sum of the first k elements
    k_element_sum = 0
    for i in range(k):
        k_element_sum += nums[i]
    
    # The current largest sum is the initial sum
    largest_sum = k_element_sum
    
    # Then SLIDE Window
    # 1. Start from index k, which is right outside 0 to k - 1 index
    for right in range(k, len(nums)):
        
        # The first element of the previous window will always be k less than
        # The last new index
        left = right - k
        
        # This does two things:
        # subtract the first element of the previous window
        # add the last element of the new window
        k_element_sum -= nums[left]
        k_element_sum += nums[right]
        
        # Then compare largest sum with this new window sum
        largest_sum = max(largest_sum, k_element_sum)
    
    return largest_sum

# Find the length of the longest substring of a given string without 
# repeating characters

def longest_substring_no_repeat_chars(string: str) -> int:
    longest = 0
    left = 0
    counter: dict[str, int] = {}

    for right in range(len(string)):
        current_string = string[right]
        counter[current_string] = counter.get(current_string, 0) + 1
        while counter[current_string] > 1:
            longest = max(longest, right - left)
            counter[string[left]] -= 1
            left += 1
    return longest

if __name__ ==  "__main__":
    # Fixed Window Example
    print('Enter a list of numbers:')
    nums = [int(x) for x in input().split()]
    k = int(input('How long do you want the list to be? '))
    res = subarray_sum_fixed(nums, k)
    print(res)
    print(longest_substring_no_repeat_chars('xyzabcaabcde'))