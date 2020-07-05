"""
20. Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""

class Solution():
    def  three_sum(self, arr):
        solution = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if(arr[i]+arr[j]+arr[k])==0:
                        solution.append([arr[i], arr[j], arr[k]])

        print(solution)

solution = Solution()
solution.three_sum([-25, -10, -7, -3, 2, 4, 8, 10])
solution.three_sum([1, 2, 3, 4, -5, -10])
