from dll import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.tracking = None

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.tracking = self.storage.head
        elif len(self.storage) == self.capacity:
            value_to_delete = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if value_to_delete == self.tracking:
                self.tracking = self.storage.tail

    def get(self):

        buffer_list = []
        tracking_node = self.tracking
        buffer_list.append(tracking_node.value)

        if tracking_node.next is not None:
            another_node = tracking_node.next
        else:
            another_node = self.storage.head

        while another_node is not tracking_node:
            buffer_list.append(another_node.value)
            if another_node.next is not None:
                another_node = another_node.next
            else:
                another_node = self.storage.head

        return buffer_list


r = RingBuffer(3)
r.append(1)
r.append(2)
r.append(3)
r.append(4)

print(r.get())
