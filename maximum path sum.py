class TrianglePath:
    def __init__(self, path):
        processed_f = open('processed_file', 'a+')
        with open(path, 'r') as file:
            for line in file.readlines():
                processed_f.writelines(line)
                processed_f.seek(0)
        self.lines = processed_f.readlines()
        processed_f.close()

    def run(self):
        print(self.lines)
        # for i, line in enumerate(self.lines):
            # for j in line.split():
                # pass


path = TrianglePath('max_path_file.txt')
TrianglePath.run(path)
