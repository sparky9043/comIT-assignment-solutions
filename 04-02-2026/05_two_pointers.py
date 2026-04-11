# Two Pointer Implementation
def is_palindrome(word: str) -> bool:
    left, right = 0, len(word) -1
    
    # This runs for as left index is smaller than the right
    while left < right:
        # if the character on the left index is not an not a number or letter, move right
        while left < right and not word[left].isalnum():
            left += 1
            
        # if the character on the right index is not an not a number or letter, move left
        while left < right and not word[right].isalnum():
            right -= 1
        
        # If the character for left and right index are not the same, return false
        if word[left].lower() != word[right].lower():
            return False
        
        # Keep moving through the indices
        left += 1
        right -= 1
    
    # return true if all characters don't return a false
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("Palindrome Checker using Two Pointers")
    print("=" * 50)
    print('Palindrome?', 'racecar', is_palindrome('racecar'))
    print('Palindrome?', 'eve', is_palindrome('eve'))
    print('Palindrome?', 'banana', is_palindrome('banana'))
    print('Palindrome?', 'panama', is_palindrome('panama'))
    print('Palindrome?', 'detartrated', is_palindrome('detartrated'))
    print('Palindrome?', 'A man, a plan, a canal: Panama', is_palindrome('detartrated'))