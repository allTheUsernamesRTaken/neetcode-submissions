# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def help(curN,prevMax):#for first node - set prevMax - Infinity
            if(curN is not None):
                #print("curN is", curN.val, "with prev at", prevMax)
                if(curN.val>=prevMax):
                    #print("above is good")
                    return 1+help(curN.left,curN.val)+help(curN.right,curN.val)
                else:
                    return help(curN.left,prevMax)+help(curN.right,prevMax)
            return 0

        return help(root,-math.inf)