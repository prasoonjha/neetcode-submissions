# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        stack = deque([])
        curr = root
        #LNR
        #[1,2,4]
        while stack or curr:
            #go as much left as possible
            while curr:
                #push curr into stack
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            #reassign curr to right
            curr = curr.right       
        return inorder