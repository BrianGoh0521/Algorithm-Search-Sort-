class Algorithm:
    def __init__(self, array):
        self.array = array

    def LinearSearch(self, target):
        for i in range(0, len(self.array)):
            if self.array[i] == target:
                print(f"{target} is in the list!")
                break
        else:
            print(f"{target} is not in the list!")

    def BinarySearch(self, target):
        i = 0
        j = len(self.array) - 1
        while i <= j:
            m = (i + j) // 2
            if self.array[m] == target:
                print(f"{target} is in the list!")
                break
            elif target < self.array[m]:
                j = m - 1
            else:
                i = m + 1
        print(f"{target} is not in the list!")

    def BubbleSort(self, order):
        print(f"Before sorted: {self.array}")
        for i in range(0, len(self.array) - 1):
            for j in range(0, len(self.array) - 1 - i):
                if order == "ascending":
                    if self.array[j] > self.array[j + 1]:
                        self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                elif order == "descending":
                    if self.array[j] < self.array[j + 1]:
                        self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        print(f"The array has been sorted in {order}!")
        print(f"After sorted: {self.array}")
        return self.array

    def BucketSort(self, order):
        pass
        #I've no idea for it's algorithm

algortihm = Algorithm([6, 5, 4, 3, 2, 1])

algortihm.LinearSearch(3)
algortihm.BinarySearch(1)
algortihm.BubbleSort("ascending")
#algortihm.BucketSort("ascending")