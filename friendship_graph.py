# Graph using adjacency list to store friendships

class Graph:
    def __init__(self):
        self.adj = {}

    def add_friendship(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start):
        visited = set()
        q = [start]
        order = []
        while q:
            node = q.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                q.extend(self.adj.get(node, []))
        return order

if __name__ == "__main__":
    g = Graph()
    g.add_friendship("Alice", "Bob")
    g.add_friendship("Bob", "Charlie")
    print("Friendship Graph:", g.adj)
    print("BFS from Alice:", g.bfs("Alice"))
