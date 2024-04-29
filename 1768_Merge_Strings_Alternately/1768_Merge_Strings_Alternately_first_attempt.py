'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating 
order, starting with word1. If a string is longer than the other, append the additional 
letters onto the end of the merged string.

Return the merged string.
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        shorter_word_length = min(len(word1), len(word2))
        # print("shorter word length is", shorter_word_length)
        longer_word_length = max(len(word1), len(word2))
        # print("longer word length is", longer_word_length)
        
        merged_string = ""
        
        for letter in range(shorter_word_length):
            merged_string = merged_string + word1[letter] + word2[letter]
            
        if len(word1) == longer_word_length: # word 1 is the longer word
            additional_letters = word1[shorter_word_length:] 
            merged_string = merged_string + additional_letters
        else: # word 2 is the longer word
            additional_letters = word2[shorter_word_length:] 
            merged_string = merged_string + additional_letters
            
        return merged_string
            
def main():
    word1 = "cats"
    word2 = "kangaroo"
    solution = Solution()
    merged_string = solution.mergeAlternately(word1, word2)
    print(merged_string)

if __name__ == "__main__":
    main()