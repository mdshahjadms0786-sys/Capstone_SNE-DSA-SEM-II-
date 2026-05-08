# User management using Hash Table for quick lookup

class UserTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, username):
        return sum(ord(c) for c in username) % self.size

    def add_user(self, username):
        h = self._hash(username)
        self.table[h].append(username)

    def search_user(self, username):
        h = self._hash(username)
        return username in self.table[h]

if __name__ == "__main__":
    ut = UserTable()
    ut.add_user("Alice")
    ut.add_user("Bob")
    print("Search Alice:", ut.search_user("Alice"))
    print("Search Charlie:", ut.search_user("Charlie"))
