# Main integration of Social Network Explorer

from user_management import UserTable
from trie_search import Trie
from friendship_graph import Graph
from posts import PostSystem

def demo():
    # Users
    ut = UserTable()
    ut.add_user("Alice")
    ut.add_user("Bob")
    ut.add_user("Charlie")

    # Trie search
    trie = Trie()
    trie.insert("Alice")
    trie.insert("Alina")

    # Friendships
    g = Graph()
    g.add_friendship("Alice", "Bob")
    g.add_friendship("Bob", "Charlie")

    # Posts
    ps = PostSystem()
    ps.add_post("Alice", "First Post!", 15)
    ps.add_post("Charlie", "Study Data Structures", 30)

    # Demo outputs
    print("Search User 'Alice':", ut.search_user("Alice"))
    print("Prefix 'Al':", trie.startsWith("Al"))
    print("BFS from Alice:", g.bfs("Alice"))
    print("Trending Post:", ps.show_trending())

if __name__ == "__main__":
    demo()



# Search User 'Alice': True
# Prefix 'Al': True
# BFS from Alice: ['Alice', 'Bob', 'Charlie']
# Trending Post: Study Data Structures
