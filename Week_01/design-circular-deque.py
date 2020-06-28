class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.data = []
        self.size = k
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.data) < self.size:
            self.data.insert(0, value)
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.data) < self.size:
            self.data.append(value)
            self.data = self.data[-self.size:]
            return True
        return False
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.data) > 0:
            self.data.pop(0)
            return True
        return False
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.data) > 0:
            self.data.pop()
            return True
        return False
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.data) > 0:
            return self.data[0]
        return -1


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.data) > 0:
            return self.data[-1]
        return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if len(self.data) == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.data) == self.size:
            return True
        return False