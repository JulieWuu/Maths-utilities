class PrimeFactor:
    def __init__(self, x):
        self.x = x
        self.answer = []

    def run(self):
        a = self.x
        for i in range(2, a):
            if a / i == a // i:
                self.answer.append(i)
                a = a / i
                if i != 1:
                    for j in range(1, int(a)):
                        if a / i == a // i:
                            self.answer.append(i)
                            a = a / i
                            j += 1
                        else:
                            break
                i += 1
            else:
                i += 1
        if a != 1:
            self.answer.append(int(a))
        return self.answer


number = PrimeFactor(99999999)
print(PrimeFactor.run(number))
