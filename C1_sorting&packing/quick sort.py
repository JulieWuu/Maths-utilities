class QuickSort:
    def __init__(self, numbers, keep=False):
        if type(numbers) is not list:
            raise TypeError
        else:
            self.numbers = numbers
        self.answer = []
        self.keep = keep
        self.done = False

        print("quick sort:")
        self.sort([self.numbers])

    def sort(self, sort_list):
        done = True
        mid_list = sort_list.copy()
        if self.keep:
            print(mid_list)
        for i, sublist in enumerate(sort_list):
            if len(sublist) > 1:
                done = False
                idx = mid_list.index(sublist)
                mid_list.remove(sublist)
                small_list = []
                large_list = []
                pivot = sublist[int(len(sublist) / 2)]
                sublist.remove(pivot)
                for num in sublist:
                    if num <= pivot:
                        small_list.append(num)
                    else:
                        large_list.append(num)
                if len(large_list) != 0:
                    mid_list.insert(idx, large_list)
                mid_list.insert(idx, [pivot])
                if len(small_list) != 0:
                    mid_list.insert(idx, small_list)

        if not done:
            self.sort(mid_list)
        else:
            for obj in mid_list:
                self.answer.append(obj[0])
            print(self.answer)
