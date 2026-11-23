# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def help(curN,prevMax):#for first node - set prevMax - Infinity
            nonlocal result
            if(curN is not None):
                #print("at",curN.val,"with prevMax",prevMax)
                if(curN.val>=prevMax):
                    #print("above is good")
                    result+=1
                    help(curN.left,curN.val)
                    help(curN.right,curN.val)
                else:
                    help(curN.left,prevMax)
                    help(curN.right,prevMax)

        help(root,-math.inf)
        return result