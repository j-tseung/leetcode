'''
Topic: Array / String
Difficulty: Easy

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

'''
May 1, 2024
Status: Complete
Time Complexity: O(n)
Space Complexity: O(n)
    - og_string O(n)
    - vowel_order O(n)
Notes: 
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = "AaEeIiOoUu"
        length = len(s)
        # print(length)
        og_string = [char for char in s]
        # print(og_string)
        vowel_order = []
        
        for x in range(length):
            # print(x)
            if og_string[x] in vowels:
                vowel_order += (og_string[x])
        
        print(vowel_order)
        
        vowel_index = len(vowel_order) - 1
        for y in range(length):
            if og_string[y] in vowels:
                og_string[y] = vowel_order[vowel_index]
                vowel_index -= 1
            
        # print(og_string)
        new_string = ''
        new_string = new_string.join(og_string)
        # print(new_string)
        return new_string
        
def main():
    s = "a."
    solution = Solution()
    solution.reverseVowels(s)
    
if __name__ == "__main__":
    main()