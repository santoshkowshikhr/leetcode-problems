class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        maj_cnt = len(nums) // 2


        for k, v in count_map.items():
            if v > maj_cnt:
                return k