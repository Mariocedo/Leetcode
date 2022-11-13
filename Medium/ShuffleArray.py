import random

class Solution:
    def __init__(self, nums: List[int]):
        self.init = nums
        self.current = list(nums)
        self.size = nums.__len__()
        return

    def reset(self) -> List[int]:
        return self.init

    # Lazy
    # def shuffle(self) -> List[int]:
    #     random.shuffle(self.current)
    #     return self.current

    # Fisher-Yates
    def shuffle(self) -> List[int]:
        for i in range(self.size):
            aux = self.current[i]
            n = random.randrange(i, self.size)
            self.current[i] = self.current[n]
            self.current[n] = aux
        return self.current