# Hash Map Implementation: Word frequency checker

def freq_checker(sentence: str) -> dict:
    # Dictionary for keeping track of each word count
    word_frequency = {}

    for word in sentence.split(" "):
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency
    
def two_sum(arr:list[int], target: int) -> list[int]:
    num_to_index = {}
    
    for i, num in enumerate(arr):
        difference = target - num
        
        if difference in num_to_index:
            return [num_to_index[difference], i]
        
        num_to_index[num] = i
        
    return []

if __name__ == "__main__":
    # A random sentence
    sentence = (
        "The quick brown fox jumps over the lazy dog while the quick fox "
        "watches another quick brown dog and the lazy dog slowly watches "
        "the fox as the brown fox jumps again and the quick dog follows "
        "the fox and the fox keeps jumping over the lazy dog again and again"
    )

    # Display all words and their counts
    word_frequency = freq_checker(sentence)
    
    print("=" * 30)
    print("Word Frequency Checker")
    print("=" * 30)
    for word, count in word_frequency.items():
        print(f"The word {word} appears {count} times.")
    print("=" * 30)
    
    nums = [2, 7, 11, 15]
    target = 9
    
    result = two_sum(nums, target)
    
    print("Two Sum checker")
    print("=" * 30)
    print("Numbers:", nums)
    print("Target:", target)
    print("Index of Two numbers:", result)
    print("Actual Numbers:", nums[0], nums[1])