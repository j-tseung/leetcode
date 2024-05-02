'''
Topic: Array / String
Difficulty: Medium

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

'''
May 2, 2024
Status: Complete
Time Complexity: O(n)
    - split() O(n)
    - for loop O(n)
Space Complexity: O(n)
    - split_string O(n)
    - reverse_string O(n)

Notes: I looked at some other solutions, I didn't know reverse() was a thing :sob:
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        
        split_string = s.split()
        length = (len(split_string))
        reverse_string = ""
        
        # print(length)
        for x in range(length):
            # print(x)
            reverse_string = reverse_string + split_string[length-x-1] + " "
        
        reverse_string = reverse_string[:(len(reverse_string)-1)]
        print(reverse_string)
        # print(type(reverse_string))
        return reverse_string

def main():
    s = "the sky is blue"
    solution = Solution()
    solution.reverseWords(s)
    
if __name__ == "__main__":
    main()