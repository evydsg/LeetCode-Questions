class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        answer = []

        map_array = {}

        for index in range(len(nums)):
            difference = target - nums[index]

            if difference in map_array:
                answer.append(index)
                answer.append(map_array[difference])

            map_array[nums[index]] = index

        return answer