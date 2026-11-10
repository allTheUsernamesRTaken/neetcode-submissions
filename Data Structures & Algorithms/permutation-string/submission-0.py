from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        width = len(s1)
        key = Counter(s1)
        remaining = Counter(s1)
        #start, need check mids, first width val
        frontI = 0
        backI = 0
        #print("key is" , key)
        while(frontI<len(s2)):
            front = s2[frontI]
            if(front not in key):
                for bi in range(backI, frontI+1):
                    #print("tryed adding back", s2[bi])
                    if(s2[bi] in key):
                        #print("adding back", s2[bi])
                        remaining[s2[bi]]+=1
                #print("not valid letter reset:",remaining)
                frontI+=1
                backI=frontI
            else: #same letters
                if(remaining[front]<=0):#too much fronts
                    for bi in range(backI, frontI+1):
                        remaining[s2[bi]]+=1
                        if(s2[bi]==front): #got to the valid part
                            backI=bi+1
                            break;
                        backI=bi+1
                    #print("too many repeats:",remaining)
                else: #still fronts left, front is valid
                    remaining[front]-=1
                    if(frontI-backI+1==width):
                        return True
                    frontI+=1
                    #print("valid:",remaining)
                    #print("now its same len:",remaining, 'at', frontI,"-",backI)
        return False
        