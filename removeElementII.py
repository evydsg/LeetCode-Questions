class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k, index = 0, 0

        for index in range(len(nums)):

            if index==0 or nums[index] != nums[index-1]:
                nums[k] = nums[index]
                k+=1

    
        return k