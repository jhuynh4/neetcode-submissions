class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1): #at each i, add flight to route, do not add flight if i exceed num flights from src (BFS)
            tmpPrices = prices.copy()
            for s, d, p in flights: #src, dst, price
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float('inf') else prices[dst]