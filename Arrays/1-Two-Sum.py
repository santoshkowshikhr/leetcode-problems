class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, n in enumerate(nums):
            comp = target - n

            if comp in nums_dict:
                return [nums_dict[comp], i]
            
            nums_dict[n] = i
        return None
