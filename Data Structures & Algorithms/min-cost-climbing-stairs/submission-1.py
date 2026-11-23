class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #[1,2,1,2,1,1,1]  STORE LOWEST CUMULATIVE COST
        #[1,2,1,2,1,1,1]  for given step - ur either 1 or 2 back
        #lowest cumul cost - is thus self+min(prev1 or prev2)
        #[1,3,2,4,3,4,4]
        if(len(cost)==2):
            return min(cost[0],cost[1])
        for i in range(2,len(cost)):
            a,b = cost[i-1],cost[i-2]
            cost[i]=cost[i]+min(a,b)
        return min(cost[-1],cost[-2])
