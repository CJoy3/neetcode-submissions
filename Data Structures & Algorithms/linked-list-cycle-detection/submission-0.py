# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []


        def dfs(self, cur: Optional[ListNode]) -> bool:
            if cur == None:
                return False
            else:
                if cur in visited:
                    return True
                else:
                    visited.append(cur)
                    return dfs(self, cur.next)
    
        return dfs(self, head)