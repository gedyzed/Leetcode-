class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
          
    def get(self, index: int) -> int:
        
        current = self.head
        count, val = 0, -1
  
        while current:
            if count == index:
                val = current.val 
            count += 1 
            current = current.next

        return val        

    def addAtHead(self, val: int) -> None:

        dummy = ListNode(0, self.head)
        current = dummy
        node = ListNode(val, current.next)
        current.next = node
        if node.next == None:
            self.tail = node

        self.head = dummy.next    


    def addAtTail(self, val: int) -> None:

        node = ListNode(val)
        if self.tail:
            self.tail.next = node
            self.tail = node

        else:  
            self.tail = node
            self.head = node 

        print('after')
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next      
        
    def addAtIndex(self, index: int, val: int) -> None:

        dummy = ListNode(0, self.head)
        current = dummy
        node = ListNode(val)
        count = -1
      
        while count < index - 1 and current:
            count += 1
            current = current.next


        added = False
        if current:
            node.next = current.next
            current.next = node 
            added = True
        
        if added:
            self.head = dummy.next  
            if not node.next:
                self.tail = node  
        
        # print('after')
        # temp = self.head
        # while temp:
        #     print(temp.val)
        #     temp = temp.next    

    def deleteAtIndex(self, index: int) -> None:

        dummy = ListNode(0, self.head)
        current = dummy
        count = -1

        while count < index - 1 and current:
            count += 1
            current = current.next

        if current and current.next:
            if not current.next.next:
                self.tail = current
    
            current.next = current.next.next

        self.head = dummy.next  
   
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)