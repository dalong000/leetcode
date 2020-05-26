class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i =0
        j =0
        for x in nums:
            j =0
            for y in nums:
                
                if(x+y==target and i!=j):
                    print(nums(i),nums(j))
                    return [i,j]
                j=j+1
            i=i+1


se = Solution()
n=[3,2,4]
t=6
se.twoSum(n,t)
