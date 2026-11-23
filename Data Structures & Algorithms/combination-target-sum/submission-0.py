class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        #at index u can either choose self, or skip for next (can be done until invalid btw repeat allowed)
        result =[]
        curL = []
        def help(i,curSum):
            if(i==len(nums)):
                return
            #print(curL,curSum)
            if(curSum<=target):#stop if too big
                #print("cursum", curSum, "=/=",target)
                if(curSum==target):#dont add more
                    result.append(curL.copy())
                    #print("result foudn")
                    return
                #below target
                curL.append(nums[i]) #add self
                help(i,curSum+nums[i])
                curL.pop()
                help(i+1,curSum)#ignore self
        help(0,0)
        return result

