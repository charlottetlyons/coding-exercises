class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _sink_down(self, index):
        min_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]:
                min_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]:
                min_index = right_index

            if min_index is not index:
                self.swap(min_index, index)
                index = min_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self.swap(current, self._parent(current))
            current = self._parent(current)

    # TODO: revise test
    def remove(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return min_value

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
