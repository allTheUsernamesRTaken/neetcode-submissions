class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curL = []
        
        def help(remaining):
            if(len(remaining)==0):
                result.append(curL.copy())
                #curL.pop()
            for i in range(len(remaining)):
                newL = remaining.copy()
                curL.append(remaining[i])
                newL.pop(i)
                help(newL)
                curL.pop()
        help(nums)
        return result

        
