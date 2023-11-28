class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        k = 0

        for index in range(len(nums)):
            
            if nums[index] != val:
                num = nums[index]
                nums[k] = num
                k+=1
            
            
        
        return k