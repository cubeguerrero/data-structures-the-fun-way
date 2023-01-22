# Max Heap
class Heap:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def add(self, item):
        self.items.append(item)

        current = len(self.items) - 1
        parent = current // 2
        while parent >= 1 and (self.items[parent] < self.items[current]):
            self.items[parent], self.items[current] = self.items[current], self.items[parent]
            current = parent
            parent = current // 2

    def pop(self):
        if len(self.items) == 0:
            return None

        max_index = len(self.items) - 1
        self.items[0], self.items[max_index] = self.items[max_index], self.items[0]
        result = self.items.pop()
        max_index = len(self.items) - 1

        i = 0
        while i <= max_index:
            swap = i
            if 2*i <= max_index and (self.items[swap] < self.items[2*i]):
                swap = 2*i

            if 2*i+1 <= max_index and (self.items[swap] < self.items[2*i+1]):
                swap = 2*i+1

            if i != swap:
                self.items[i], self.items[swap] = self.items[swap], self.items[i]
                i = swap
            else:
                break

        return result


if __name__ == '__main__':
    heap = Heap()
    heap.add(99)
    heap.add(5)
    heap.add(50)
    heap.add(97)
    heap.add(98)
    print(heap)
    heap.pop()
    print(heap)
