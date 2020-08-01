class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

        elif value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    def contains(self, target):
        if self.value == target:
            return True

        if target > self.value:
            if self.right is not None:
                return self.right.contains(target)

        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)

        else:
            return False
