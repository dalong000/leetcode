class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1 ==[]  :
            if len(nums2) == 1:
                return nums2[0]
            elif len(nums2) == 2:
                return (float(nums2[0])+float(nums2[1])) / 2
            else:
                if len(nums2) % 2 == 1:
                    return nums2[int(len(nums2) / 2)]
                else:
                    return (float(nums2[int(len(nums2) / 2)]) + float(nums2[int(len(nums2) / 2- 1) ])) /2
        if nums2 ==[]  :
            if len(nums1) == 1:
                return nums1[0]
            elif len(nums1) == 2:
                return (float(nums1[0])+float(nums1[1])) / 2
            else:
                if len(nums1) % 2 == 1:
                    return nums1[int(len(nums1) / 2)]
                else:
                    return (float(nums1[int(len(nums1) / 2)]) + float(nums1[int(len(nums1) / 2 - 1)])) /2
        nums1len = len(nums1)
        nums2len = len(nums2)

        a = []
        x = 0
        y = 0
        while 1:
            if nums1[x] < nums2[y]:
                a.append(nums1[x])
                x=x+1
            else:
                a.append(nums2[y])
                y=y+1
            if x == nums1len:
                while y<nums2len:
                    a.append(nums2[y])
                    y=y+1
                break
            if y == nums2len:
                while x<nums1len:
                    a.append(nums1[x])
                    x=x+1
                break

        if len(a) % 2 == 1:
            return a[int(len(a) / 2)]
            
        else:
            print(a[int(len(a) / 2)])
            print(a[int(len(a) / 2 - 1) ])
            x = 1.0
            x = (float(a[int(len(a) / 2)]) +float(a[int(len(a) / 2 - 1) ])) / 2
            print(x)
            return x

se = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(se.findMedianSortedArrays(nums1,nums2))