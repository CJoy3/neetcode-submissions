# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def bfs(startNode: Optional[TreeNode]) -> List[Optional[TreeNode]]:
            queue = []
            visited = []
            if startNode:
                visited.append(startNode.val)
                queue.append(startNode)
            else:
                visited.append(None)
            

            while len(queue) > 0:
                currentNode = queue.pop(0)
                if currentNode.left != None:
                    visited.append(currentNode.left.val)
                    queue.append(currentNode.left)
                else:
                    visited.append(None)
                if currentNode.right != None:
                    visited.append(currentNode.right.val)
                    queue.append(currentNode.right)
                else:
                    visited.append(None)
            
            return visited

        pTraversal = bfs(p)
        qTraversal = bfs(q)

    

        return pTraversal == qTraversal



        