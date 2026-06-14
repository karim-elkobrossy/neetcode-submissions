class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            ordered_stones = sorted(stones, reverse=True)
            y = ordered_stones[0]
            x = ordered_stones[1]
            if x == y:
                stones.remove(x)
                stones.remove(y)
            else:
                # if not equal, y is always bigger than x (first element in sorted list)
                stones.remove(x)
                stones.remove(y)
                stones.append(y-x)
        if not stones: return 0
        else: return stones[0]

            