class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:

        leftPrefix = left
        index = 0
        sum = 0

        while left <= right:
            sum += self.nums[left]
            left +=1
        
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)