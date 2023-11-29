class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0

        for index in range(len(nums)-1):
            if nums[index] != nums[index+1]:
                nums[k] = nums[index]
                k+=1

        nums[k] = nums[-1]
        k += 1

        return k