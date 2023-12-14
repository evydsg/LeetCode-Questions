 def __init__(self, nums: List[int]):
        self.nums = nums
        sum = 0
        self.prefix = []

        for num in nums:
            sum += num
            self.prefix.append(sum)


    def sumRange(self, left: int, right: int) -> int:
        rightS = self.prefix[right]

        if left > 0:
            leftS = self.prefix[left-1] 
        else:
            leftS = 0

        return rightS - leftS
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)