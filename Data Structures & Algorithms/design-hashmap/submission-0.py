class MyHashMap:

    def __init__(self):
        self.cache = {}

    def put(self, key: int, value: int) -> None:
        
        self.cache[key] = value

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.cache[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.cache:
            del self.cache[key]
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)