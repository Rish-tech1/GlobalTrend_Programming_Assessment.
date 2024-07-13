class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, value):
        if value not in self.heap:
            raise ValueError("Value not found in the heap")
        idx = self.heap.index(value)
        self.heap[idx] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(idx)

    def get_max(self):
        if not self.heap:
            raise ValueError("Heap is empty")
        return self.heap[0]

    def _heapify_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[parent_idx] >= self.heap[idx]:
                break
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx

    def _heapify_down(self, idx):
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            largest_idx = idx
            if left_child_idx < len(self.heap) and self.heap[left_child_idx] > self.heap[largest_idx]:
                largest_idx = left_child_idx
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] > self.heap[largest_idx]:
                largest_idx = right_child_idx
            if largest_idx == idx:
                break
            self.heap[idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[idx]
            idx = largest_idx

# Example usage:
heap = MaxHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)
heap.insert(2)

print(heap.get_max())  
heap.delete(3)
print(heap.get_max()) 

heap.insert(10)
print(heap.get_max()) 

heap.delete(8)
print(heap.get_max())  