import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distances = []
        # for i, point in enumerate(points):
        #     x1, y1 = point[0], point[1]
        #     x2, y2 = 0, 0
        #     distance_to_origin = (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
        #     distances.append((i, distance_to_origin))
        #     print(x1, y1, distance_to_origin)
        # distances.sort(key=lambda x: x[1])
        # return [points[distance[0]]for distance in distances[:k]]
        distance_heap = []
        result = []
        for i, point in enumerate(points):
            x1, y1 = point[0], point[1]
            x2, y2 = 0, 0
            distance_to_origin = (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
            distance_heap.append((distance_to_origin, point))
        heapq.heapify(distance_heap)
        for i in range(k):
            result.append(heapq.heappop(distance_heap)[1])
        return result
