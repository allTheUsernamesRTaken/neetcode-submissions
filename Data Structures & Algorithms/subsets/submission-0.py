class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #[1,2,3]
        #[1,2]
        result = []
        cur = []
        def help(i):
            if(i==len(nums)):
                result.append(cur.copy())
                return
            cur.append(nums[i]) #add smth new timeline
            help(i+1)
            cur.pop()
            help(i+1)

        help(0)
        return result