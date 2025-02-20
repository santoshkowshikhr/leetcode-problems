# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def build_tree(left, right):       
            if left > right:
                return None

            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])

            root.left = build_tree(left, mid -1)
            root.right = build_tree(mid+1, right)

            return root
        
        return build_tree(0, len(nums)-1)

        