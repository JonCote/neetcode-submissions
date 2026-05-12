class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [x * -1 for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if x == y:
                heapq.heappush(maxHeap, 0)

            else:
                heapq.heappush(maxHeap, (y - x)*-1)
                
        
        return heapq.heappop(maxHeap) * -1


