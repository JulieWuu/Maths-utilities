class Fibonacci:
    def __init__(self, upper):
        self.upper = upper
        self.numbers = []

    def run(self):
        f0 = 0
        f1 = 1
        self.numbers.append(f1)
        i = 2
        while True:
            f2 = f0 + f1
            if f2 <= self.upper:
                self.numbers.append(f2)
                i += 1
                f0 = f1
                f1 = f2
            else:
                break

        return self.numbers


fibonacci = Fibonacci(100)
print(fibonacci.run())
