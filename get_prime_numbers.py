class PrimeNumber:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.answer = []

    def run(self):
        if int(self.lower) != self.lower or int(self.upper) != self.upper:
            raise TypeError
        if self.lower < 0 or self.upper <= self.lower:
            raise ValueError

        if self.lower <= 2:
            self.answer.append(2)
        b = 0
        for a in range(self.lower + 1, self.upper + 1):
            for i in range(2, a):
                if a / i == a // i:
                    b = a / i
                    break
                else:
                    b = a
            if b == a:
                self.answer.append(b)
        return self.answer


bound = PrimeNumber(99999900, 100000000)
print(bound.run())
