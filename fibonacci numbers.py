class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.numbers = []

    def run(self):
        f0 = 0
        f1 = 1
        self.numbers.append(f1)
        i = 2
        while True:
            f2 = f0 + f1
            if f2 <= self.limit:
                self.numbers.append(f2)
                i += 1
                f0 = f1
                f1 = f2
            else:
                break

        return self.numbers

    def even_sum(self):
        even_sum = 0
        f0 = 0
        f1 = 1
        i = 2
        while True:
            f2 = f0 + f1
            if f2 <= self.limit:
                if f2 % 2 == 0:
                    even_sum += f2
                i += 1
                f0 = f1
                f1 = f2
            else:
                return even_sum


print(Fibonacci(4000000).even_sum())
