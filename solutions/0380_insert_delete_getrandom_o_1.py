import random

class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.pos = {}
    def insert(self, val: int) -> bool:
        if val in self.pos: return False
        self.pos[val] = len(self.arr); self.arr.append(val); return True
    def remove(self, val: int) -> bool:
        if val not in self.pos: return False
        i = self.pos.pop(val); last = self.arr.pop()
        if i < len(self.arr):
            self.arr[i] = last; self.pos[last] = i
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)
