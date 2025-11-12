class BubbleSort:
    def __init__(self, numbers, keep=False):
        if type(numbers) is not list:
            raise TypeError
        else:
            self.numbers = numbers
        self.answer = []
        self.keep = keep

        print("bubble sort:")
        self.sort(self.numbers)
        print(self.answer)

    def sort(self, start_list):
        if self.keep:
            print(start_list + self.answer)
        end_list = []

        if len(start_list) == 1:
            self.answer.insert(0, start_list[-1])
            return self.answer
        else:
            mid_list = start_list.copy()
            for i in range(len(start_list) - 1):
                end_list = mid_list.copy()
                if mid_list[i] > mid_list[i + 1]:
                    end_list[i] = mid_list[i + 1]
                    end_list[i + 1] = mid_list[i]
                    mid_list = end_list

            if end_list == start_list:
                for i in range(len(end_list)):
                    self.answer.insert(0, end_list[-1])
                    end_list = end_list[:-1]
                return self.answer
            else:
                self.answer.insert(0, mid_list[-1])
                self.sort(end_list[:-1])
