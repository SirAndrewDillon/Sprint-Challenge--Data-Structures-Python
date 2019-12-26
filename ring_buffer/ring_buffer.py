from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.switch = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == self.storage.length:
          self.storage.remove_from_head()
        self.storage.add_to_tail(item)
        if self.switch > 0 and self.switch%self.capacity == 0:
          self.current = self.storage.tail
        self.switch += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if self.current:
          list_buffer_contents.append(self.current.value)
          while self.current.next:
            self.current = self.current.next
            list_buffer_contents.append(self.current.value)
        if len(list_buffer_contents) < self.storage.length:
          node = self.storage.head
          list_buffer_contents.append(node.value)
          while node.next and len(list_buffer_contents) < self.storage.length:
            node = node.next
            list_buffer_contents.append(node.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass