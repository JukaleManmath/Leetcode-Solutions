class RandomizedSet:

    def __init__(self):
        # self.set = set()
        self.values = []
        self.index = {}

    def insert(self, val: int) -> bool:
        # flag = False
        # if val not in self.set:
        #     flag = True
        #     self.set.add(val)
        # return flag

        if val in self.index:
            return False
        
        self.index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        idx = self.index[val]
        self.index[self.values[-1]] = idx
        del self.index[val]
        self.values[idx] = self.values[-1]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        index = random.randint(0,len(self.values)-1)
        return self.values[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()