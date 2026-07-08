# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

            visited = []

            def dfs(sNode: Optional[TreeNode]):
                if sNode:
                    visited.append(sNode.val)

                if sNode.left and sNode.left not in visited:
                    dfs(sNode.left)
                if sNode.right and sNode.right not in visited:
                    dfs(sNode.right)

            dfs(subRoot)
            subTrav = visited

            queue = []
            queue.append(root)

            while queue:
                currentNode = queue.pop(0)

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right: 
                    queue.append(currentNode.right)
                visited = []
                dfs(currentNode)
                if visited == subTrav:
                    return True
            return False
            





            