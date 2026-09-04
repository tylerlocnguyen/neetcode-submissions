class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.topKNums = []
        self.k = k
        for num in nums:
            self.add(num)




    def add(self, val: int) -> int:
        if len(self.topKNums) < self.k:
            heapq.heappush(self.topKNums, val)
        else:
            #is in topk
            if val > self.topKNums[0]:
                heapq.heappop(self.topKNums)
                heapq.heappush(self.topKNums, val)

        
        return self.topKNums[0]

