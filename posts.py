# Posts stored in a simple list + trending using heap

import heapq

class PostSystem:
    def __init__(self):
        self.posts = []
        self.trending = []

    def add_post(self, user, content, likes):
        self.posts.append((user, content, likes))
        # use negative likes for max-heap
        heapq.heappush(self.trending, (-likes, content))

    def show_trending(self):
        if self.trending:
            return heapq.heappop(self.trending)[1]
        return None

if __name__ == "__main__":
    ps = PostSystem()
    ps.add_post("Alice", "Hello World!", 10)
    ps.add_post("Bob", "Good Morning!", 25)
    print("Trending Post:", ps.show_trending())
