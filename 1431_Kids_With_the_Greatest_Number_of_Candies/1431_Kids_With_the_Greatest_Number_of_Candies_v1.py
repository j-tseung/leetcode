'''
Topic: Array / String
Difficulty: Easy

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
'''

'''
April 30, 2024
Status: Compelete
Time Complexity: O(n)
    - max(candies) is computed once, taking O(n).
    - Looping through the candies list once, which also takes O(n).
Space Complexity: O(n)
    - The space required for the 'greatest' list, which has the same length as the input list 'candies'.
'''

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        greatest = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                greatest.append(True)
            else: 
                greatest.append(False)
        
        # print(*greatest, sep = ", ") 
        return greatest
                
def main():
    candies = [2,3,5,1,3]
    extraCandies = 3
    solution = Solution()
    solution.kidsWithCandies(candies, extraCandies)
    
if __name__ == "__main__":
    main()