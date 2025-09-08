class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []

        def change(p , t):
            return (p + 1) / (t + 1) -  (p / t)
        
        for p , t in classes:
            heap.append((-change(p,t), p , t))
        heapq.heapify(heap)

        for _ in range(extraStudents):
            curr, p , t = heapq.heappop(heap)
            heapq.heappush(heap,(-change(p + 1, t + 1), p + 1, t + 1))

        total = sum (x / y for _, x , y in heap)
        return total / len(classes)
