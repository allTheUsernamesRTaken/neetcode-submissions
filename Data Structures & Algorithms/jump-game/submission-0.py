class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #land on 0 and its over - avoid 0s at all costs
        #[1,2,0,1,0]
        # if 2 nums - clearly the num with most coverage is optimal - as all other nums moves are just subsets of that num
        i=0
        while (i<len(nums)):
            if(i>=len(nums)-1):
                return True
            allowedSteps = nums[i]
            maxNewIndex = min(allowedSteps+i, len(nums)-1) #max index reached
            if(nums[i]==0): #not at the ending, stuck on 0, assume optimal?
                print("on 0 now")
                return False
            maxReach = 0;
            optimalI = i;
            for testIndex in range(i+1, maxNewIndex+1): #try new indices
                testIndexReach = nums[testIndex]+testIndex
                if(testIndexReach>maxReach):
                    optimalI=testIndex #find furthest index
                    maxReach = testIndexReach
            i = optimalI
        return False


                