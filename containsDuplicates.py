class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = set()

        for index in nums:
            if index in unique:
                return True
            unique.add(index)
        
        return False