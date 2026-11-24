class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals)==1):
            return intervals
        intervals.sort()
        result = [intervals[0]]
        for i in range(0, len(intervals)): #skip last
            cItv = intervals[i]
            start,end = cItv[0],cItv[1]
            curItv = result[-1]
            curStart,curEnd = curItv[0],curItv[1]
            if(start<=curEnd):# overlap, all 
                if(end>curEnd):
                    result[-1][1] = end
            else: #maybe interior
                result.append(cItv)
        return result