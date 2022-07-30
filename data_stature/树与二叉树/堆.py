# https://blog.csdn.net/qq_23869697/article/details/82735088#t3

class Array:
    """自定义数组"""

    def __init__(self, size=32):
        self.size = size
        self._items = [None]*size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __len__(self):

        return len(self._items)

    def clear(self, value=None):
        """重置数组为空"""

        for i in range(self.size):
            self._items[i] = None

    def __iter__(self):
        for item in self._items:
            yield item

    def __delitem__(self, key):

        del self._items[key]


class MaxHeap:
    """最大堆"""

    def __init__(self, maxsize=None):

        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0  # 记录索引

    def __len__(self):
        return self._count

    def add(self, value):
        """添加元素"""

        if self._count >= self.maxsize:
            raise Exception("Heap has fulled!")

        self._elements[self._count] = value
        self._count += 1
        self._shiftup(self._count - 1)  # 对插入结点进行堆化

    def _shiftup(self, ndx):
        """插入堆化"""

        if ndx > 0:
            parent = int((ndx-1)/2)
            if self._elements[ndx] > self._elements[parent]:
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                #  递归继续调整位置
                self._shiftup(parent)

    def extract(self):

        if self._count<=0:
            raise  Exception("Heap is empty!")
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        del self._elements[self._count] # 删除最后一个结点元素的值
        self._shiftdown(0)
        return value

    def _shiftdown(self, ndx):

        left = 2*ndx + 1
        right = 2*ndx + 2

        largest = ndx

        if left < self._count and self._elements[left] >= self._elements[largest]:
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            #  向下递归，调整结构
            self._shiftdown(largest)

    def show(self):
        return  self._elements


if __name__ == "__main__":
    array =[2, 5, 88, 3, 9]
    heap = MaxHeap(5)
    for i in array:
        heap.add(i)
    for x in heap.show():
        print(x)
    heap.extract()
    print("*"*10)
    for x in heap.show():
        print(x)