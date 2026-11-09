import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sHeap = []
        for s in stones:
            sHeap.append(-s)
        
        heapq.heapify(sHeap)

        while(len(sHeap)>1):
            biggest = heapq.heappop(sHeap)
            secondBig = heapq.heappop(sHeap)
            heapq.heappush(sHeap, biggest-secondBig)
        return -sHeap[0]
        