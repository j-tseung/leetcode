'''
Topic: Array / String
Difficulty: Easy

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''

'''
May 1, 2024
Status: Complete
Time Complexity: O(n)
Space Complexity: O(1)
Notes: The most brute force method I could think of
'''
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        viable = 0 # number of viable flowers that can be planted
        
        # no flower bed
        if length == 0: return False
        
        # 1 flower bed
        elif length == 1:
            if flowerbed[0] == 0 and n <= 1: return True 
            else: False    
        x = 0    
        while x <= length-1:
            print("x is", x)
            if x == 0:
                if flowerbed[x] == 0:
                    if flowerbed[x+1] == 0: 
                        viable += 1
                        print(f"can put in flowerbed[{x}]")
                        x = x + 2
                    else: x += 1
                else: x += 1
            elif x == length-1:
                if flowerbed[x] == 0:
                    if flowerbed[x-1] == 0:
                        viable += 1
                        print(f"can put in flowerbed[{x}]")
                        x = x + 2
                    else: x += 1
                else: x += 1
            else:
                if flowerbed[x] == 0:
                    if flowerbed[x-1] == 0 and flowerbed[x+1] == 0:
                        viable +=1
                        print(f"can put in flowerbed[{x}]")
                        x = x + 2
                    else: x += 1
                else: x += 1
            
        print(n, viable)
        print(n <= viable) 
        return(n <= viable)    
        

def main():
    flowerbed = [1,0,0,0,1]
    n = 1
    solution = Solution()
    solution.canPlaceFlowers(flowerbed, n)
    
if __name__ == "__main__":
    main()