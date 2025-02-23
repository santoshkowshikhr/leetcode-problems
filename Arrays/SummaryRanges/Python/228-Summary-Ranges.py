class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0


        for j in range(1, len(nums) + 1):
            if j == len(nums) or nums[j] != nums[j-1]+1:
                if i == j - 1:
                    res.append(str(nums[i]))
                else:
                    res.append(f\{nums[i]}->{nums[j-1]}\)
                
                i = j

        return res
        