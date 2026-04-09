import heapq as pq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]

        ak= []

        
        dist = [float('inf') ] * (n+1)
        dist[k] = 0

        for u , v ,w in times:
            adj[u].append((v,w))
        
        pq.heappush(ak,(0,k))

        while ak:
            curr_dist ,node = pq.heappop(ak)
            if curr_dist > dist[node]:
                continue
           
            for neighbor ,weight in adj[node]:
                new_dist =curr_dist + weight
                
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    pq.heappush(ak,(new_dist ,neighbor))

        result  = max(dist[1:])
        return result if result != float('inf') else -1

        

        