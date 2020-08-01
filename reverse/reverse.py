class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head == None:  # empty list test
            return None
        else:
            cur_node = self.head  # take head node and save value
            next_node = cur_node.next_node  # set next node to current heads next node value
            # set current heads or node next attribute to none as it will become tail in reverse
            cur_node.set_next(None)
            self.tail = cur_node  # set tail to the cur node
            while next_node is not None:  # while we still have nodes in the list
                prev_node = cur_node  # prev or first node was our current
                cur_node = next_node  # set cur node to our saved next
                next_node = cur_node.next_node  # set our next to the currents next
                # point node to the new tail or new node depending on loop
                cur_node.set_next(prev_node)

            self.head = cur_node    # last node before loop breaks will now be our head
