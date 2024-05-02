'''
For two strings s and t, we say "t divides s" if and only if 
s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''
# answer based on hints provided and editoral approach 1
# April 30, 2024
# Status: Incomplete

import re

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1) == min(len(str1), len(str2)):
            base = str1
        else:
            base = str2
                
        # check if str1 is made of multiples of base
        string = str1
        
        while True:
            solution = Solution.check_string(base, string)
        
        
             


    def check_string(base, string):
        print("checking string of length", len(string))
        for x in range(len(base)):
            
            if base[x] == string [x]:
                print("base", base[x], "matches string", string[x])
            else:
                print("base", base[x], "does not match string", string[x])
        
        string = string[len(base):]
        
        if base in string:
            return 1 # base is gcd
        else:
            return 0 # indicates base is not GCD
        print(string)



def main():
    str1 = "ABCABCABC"
    str2 = "ABCABC"
    solution = Solution()
    solution.gcdOfStrings(str1, str2)
    # s = 'ABACABAC'
    # print(s.replace('ABAC', ''))
    
    # print(str1[3:])

    
    
    
if __name__ == "__main__":
    main()