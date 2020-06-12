class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenmax = 0
        if s == " " or len(s) == 1 :
            return 1
        if len(s) == 2:
            if s[0] == s[1]:
                return 1
        if s is None or len(s) == 0:
            return 0
        for i in range(len(s)): 
            b = []
            smax = 0
            for j  in range(i,len(s)):
                if s[j] in b:  
                    if smax>lenmax:
                        lenmax=smax
                    break
                else:
                    smax = smax+1
                    b.append(s[j])
                    if smax>lenmax:
                        lenmax=smax
            
            
        return lenmax