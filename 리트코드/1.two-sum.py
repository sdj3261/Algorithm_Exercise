from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

s = Solution()
num = [1,2,3,4,5,6,7,8,9]
target = 5
print(s.twoSum(num,target))



