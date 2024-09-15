class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return max_val

    def _sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def _sift_down(self, i):
        max_index = i
        left = self.left_child(i)
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        right = self.right_child(i)
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
        if i != max_index:
            self.swap(i, max_index)
            self._sift_down(max_index)

    def is_empty(self):
        return len(self.heap) == 0

# Example usage:

# Task scheduling
print("Task Scheduling Example:")
task_queue = PriorityQueue()
task_queue.insert((3, "Low priority task"))
task_queue.insert((5, "Medium priority task"))
task_queue.insert((7, "High priority task"))

while not task_queue.is_empty():
    priority, task = task_queue.extract_max()
    print(f"Executing: {task} (Priority: {priority})")

print("\nEmergency Room Triage Example:")
# Emergency Room Triage
er_queue = PriorityQueue()
er_queue.insert((2, "Minor cut"))
er_queue.insert((5, "Broken arm"))
er_queue.insert((10, "Heart attack"))
er_queue.insert((8, "Severe bleeding"))

while not er_queue.is_empty():
    severity, condition = er_queue.extract_max()
    print(f"Treating patient with: {condition} (Severity: {severity})")

print("\nNetwork Packet Routing Example:")
# Network Packet Routing
packet_queue = PriorityQueue()
packet_queue.insert((1, "Data packet"))
packet_queue.insert((3, "Voice packet"))
packet_queue.insert((2, "Video packet"))

while not packet_queue.is_empty():
    priority, packet_type = packet_queue.extract_max()
    print(f"Routing: {packet_type} (Priority: {priority})")