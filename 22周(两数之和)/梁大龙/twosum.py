

def twoSum(nums, target):

    hashmap = {}

    for index, num in enumerate(nums):
      
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num], index]
        hashmap[num] = index
        
 
    return None

print(twoSum([1,4,7,9],11))
