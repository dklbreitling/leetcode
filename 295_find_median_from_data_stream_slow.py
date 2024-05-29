class MedianFinder:

    def __init__(self):
        self.arr = []
        self.median = None
        self.new_median = True
        

    def addNum(self, num: int) -> None:
        inserted = False
        if len(self.arr) == 0 or num >= self.arr[-1]:
            self.arr.append(num)
            inserted = True
        elif num <= self.arr[0]:
            self.arr = [num] + self.arr
            inserted = True

        curr_index = len(self.arr) // 2
        found = False
        step = len(self.arr) // 4
        while not inserted:
            if self.arr[curr_index] > num:  # go left
                curr_index -= max(step, 1)
            elif self.arr[curr_index] < num:  # go right
                curr_index += max(step, 1)
            if self.arr[curr_index] <= num and self.arr[curr_index + 1] >= num:
                self.arr = self.arr[:curr_index + 1] + [num] + self.arr[curr_index + 1:]
                inserted = True
            step //= 2

        self.new_median = True


    def findMedian(self) -> float:
        if not self.new_median:
            return self.median
        if (l_arr := len(self.arr)) % 2 == 0:
            self.median = (self.arr[int(l_arr / 2 - 1)] + self.arr[int(l_arr / 2)]) / 2
        else:
            self.median = self.arr[l_arr // 2]
        self.new_median = False
        return self.median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

