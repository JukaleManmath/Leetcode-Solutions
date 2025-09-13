class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        flag = False
        if val not in self.set:
            flag = True
            self.set.add(val)
        return flag

    def remove(self, val: int) -> bool:
        flag = True
        if val not in self.set:
            flag = False
        else:
            self.set.remove(val)
        return flag

    def getRandom(self) -> int:
        return random.choice(tuple(self.set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()