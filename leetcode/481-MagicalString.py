class Solution:
    def update_string(self):
        key = self.s1[self.counter]
        last_key = self.s1[-1]
        if last_key == 1:
            self.s1 += [2] * key
        else:
            self.s1 += [1] * key
        self.counter += 1
        # print(self.s1)
    
    def magicalString(self, n: int) -> int:
        self.s1 = [1, 2, 2]
        self.counter = 2
        print(self.s1)
        while len(self.s1) < n:
            self.update_string()
        return self.s1[:n].count(1)