class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #land on 0 and its over - avoid 0s at all costs
        #[1,2,0,1,0]
        # if 2 nums - clearly the num with most coverage is optimal - as all other nums moves are just subsets of that num
        maxIndexReach = 0;
        for i, n in enumerate(nums):
            if(i>maxIndexReach): #as linear, if one square unreachable - all after is also 
                return False
            maxIndexReach = min(max(maxIndexReach, i+n), len(nums)-1)
        if(maxIndexReach==len(nums)-1):
            return True


                