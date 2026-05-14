class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for idx, num in enumerate(nums):
            value = visited.get(target-num)
            visited[num] = idx
            if (value != None):
                return [value, idx]
            

            