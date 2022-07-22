#Solution 1 Time limit exceeded
class Solution(object):
    def twoSum(self, numbers, target):
        
        
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return i+1, j+1

#Solution 2, 179ms, 14.4mb
class Solution(object):
    def twoSum(self, numbers, target):
        
        l = 0
        r = len(numbers)-1
        
        while l<r:
            if numbers[l] + numbers[r] == target:
                return l+1, r+1
            elif numbers[l] + numbers[r] < target:        
                l += 1
            else:
                r -= 1
            