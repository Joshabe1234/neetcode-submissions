class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)

        if self.head is None:
            self.head = newNode
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        current = self.head
        i = 0
        while current:
            if i == index - 1:
                if current.next is not None:
                    current.next = current.next.next
                    return True
            current = current.next
            i += 1
        return False


    def getValues(self) -> List[int]:
        current = self.head
        values = []
        while current:
            values.append(current.val)
            current = current.next
        return values
        
