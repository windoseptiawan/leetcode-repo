class Solution(object):
    def reverseString(self, s):
        
        m = len(s)/2
        
        for l in range(m):
            s[l], s[-l-1] = s[-l-1], s[l]
        return s
      

                