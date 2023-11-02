class MyHashMap:

    def __init__(self):
        #print("=" * 10)
        self.values = [None] * 10 + [[-1] * 10]

    def access(self, key):
        "return index and list"
        d, m = divmod(key, 10)
        values = self.values
        while d != 0:
            if values[m] is None:
                values[m] = [None] * 10 + [[-1] * 10]
            values = values[m]
            d, m = divmod(d, 10)
        return m, values[-1]

    def put(self, key: int, value: int) -> None:
        m, values = self.access(key)
        values[m] = value

    def get(self, key: int) -> int:
        m, values = self.access(key)
        return values[m]

    def remove(self, key: int) -> None:
        m, values = self.access(key)
        values[m] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)