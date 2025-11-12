class TrianglePath:
    def __init__(self, file):
        self.file = []
        with open(file, 'r') as f:
            for line in f.readlines():
                self.file.append([])
                for num in line.split():
                    self.file[-1].append(int(num))
        self.file.reverse()
        print(self.file)

    def run(self):
        for i in range(1, len(self.file)):
            for j in range(len(self.file[i])):
                self.file[i][j] += max(self.file[i - 1][j], self.file[i - 1][j + 1])
        return self.file[-1][0]


print(TrianglePath('0067_triangle.txt').run())
