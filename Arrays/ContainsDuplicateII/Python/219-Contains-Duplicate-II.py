class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        comp_map = {}

        for i,v in enumerate(nums): 
            if v in comp_map and abs(i-comp_map[v]) <= k:
                    return True
                
            comp_map[v] = i
            
        return False