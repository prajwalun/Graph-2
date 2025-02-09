# The criticalConnections method finds all critical connections (bridges) in a network.

# Approach:
# - Build an adjacency list from the connections.
# - Use DFS to traverse nodes, recording their discovery times (`arrival_time`).
# - Track back edges to update the earliest reachable node.
# - If a neighbor's discovery time remains unchanged, it's a critical connection.

# TC: O(n + e) - Traverse all nodes and edges.
# SC: O(n + e) - Space for the graph and recursive stack.


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    
        graph = defaultdict(list)
        for node1, node2 in connections:
            graph[node1].append(node2), graph[node2].append(node1)
            
        arrival_time = [None]*n
        critical_connections = []
        def dfs(node = 0, parent = -1, time = 1):
            if arrival_time[node]: return
            arrival_time[node] = time
            for neighbour in graph[node]:
                if neighbour == parent: continue 
                dfs(neighbour, node, time + 1)
                if arrival_time[neighbour] == time + 1: critical_connections.append((node, neighbour))
                else: arrival_time[node] = min(arrival_time[node], arrival_time[neighbour])
            return critical_connections
        
        return dfs()