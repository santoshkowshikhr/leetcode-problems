class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_map = set()

        for num in nums:
            if num in count_map:
                return True
            else:
                count_map.add(num)
        
        return False