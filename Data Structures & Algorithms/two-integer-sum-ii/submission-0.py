class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #greedy algo - if back+front>target move back --
        #if b+f too big - move b --, too small, move f++
        fi = 0
        bi = len(numbers)-1 #if overshoot - move back by index

        while(True):
            front = numbers[fi]
            back = numbers[bi]
            if(front+back==target):
                return [fi+1,bi+1]
            if(front+back>target):
                bi-=1
            else:
                fi+=1
        
        