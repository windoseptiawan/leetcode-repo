#Solution 1 
class Solution(object):
    def sortedSquares(self, nums):
        
        res = []
        
        for num in nums:
            res.append(num**2)
        return sorted(res)

#Soluton 2
class Solution(object):
    def sortedSquares(self, nums):
        
        return sorted(num**2 for num in nums)
       

        
       
