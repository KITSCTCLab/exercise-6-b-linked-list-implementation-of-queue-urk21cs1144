class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    # Write your code here
    n = Node(data)
    if self.head is None and self.head is None:
      self.head = n
    if self.last is not None:
      self.last.next = n
    self.last = n

  def dequeue(self) -> None:
    # Write your code here
    if self.head is not None:
      self.head = self.head.next

  def status(self) -> None:
    # Write your code here
    itr = self.head
    while itr is not None:
      print(itr.data, end = "=>")
      itr = itr.next
    print("None")


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
