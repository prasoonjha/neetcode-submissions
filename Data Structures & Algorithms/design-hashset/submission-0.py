class MyHashSet:

    def __init__(self):
        self.cache = {}

    def add(self, key: int) -> None:
        if key not in self.cache:
            self.cache[key] = key

    def remove(self, key: int) -> None:
        if key in self.cache:
            del self.cache[key]
        return 

    def contains(self, key: int) -> bool:
        if key in self.cache:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)