class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = []
        t1 = x
        if x==0 :
            print(0)
        elif x > 0:
            while x > 9:
                y = x % 10
                x = (x-y) /10
                a.append(y)
            a.append(x)
            sum = 0
            for i in a:
                sum = sum *10 +i
            print(int(sum))
            
        elif x < 0 :
            x = 0 - x
            while x > 9:
                y = x % 10
                x = (x-y) /10
                a.append(y)
            a.append(x)
            sum = 0
            for i in a:
                sum = sum *10 +i
            print(int(0-sum))


se = Solution()
t=1534236469
if t < -2**31 or t > 2**31 -1:
    print(1)
se.reverse(t)
