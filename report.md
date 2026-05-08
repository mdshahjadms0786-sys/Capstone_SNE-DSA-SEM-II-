Aim: Build a mini social network using DS concepts.

Data Structures Used:

Hash Table → fast user lookup.

Trie → prefix search for usernames.

Graph → friendships + BFS traversal.

Heap → trending posts.

Complexity:

User search O(1) avg.

Trie prefix search O(length of prefix).

BFS O(V+E).

Heap insert/extract O(log n).

Demo: Shows users, friendships, posts, and trending.

# Social Network Explorer (Capstone)

## Aim
To integrate multiple data structures into a mini social network simulation.

## Data Structures Used
- Hash Table: Fast user lookup
- Trie: Prefix search for usernames
- Graph: Friendships + BFS/DFS traversal
- Heap: Trending posts

## Complexity Notes
- User search: O(1) average
- Trie prefix search: O(length of prefix)
- BFS/DFS: O(V+E)
- Heap insert/extract: O(log n)

## Demo
- Added users: Alice, Bob, Charlie
- Friendships: Alice-Bob, Bob-Charlie
- Posts: Alice (15 likes), Charlie (30 likes)
- Output shows user search, prefix search, BFS traversal, and trending post.
