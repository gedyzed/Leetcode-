class Node:
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pointers = {}

        #dummy nodes 
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:

        if key not in self.pointers:
            return -1

        node = self.pointers[key]
        self.remove(node)
        self.insert(node)
        return node.val
          

    def remove(self, node):
        
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        key = node.key 
        self.pointers.pop(key)
       
    def insert(self, node):

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        
        key = node.key
        self.pointers[key] = node

    def put(self, key: int, value: int) -> None:
        if key in self.pointers:
            node = self.pointers[key]
            node.val = value
            self.remove(node) 
            self.insert(node)

        else:
            new_node = Node(key, value)
            if len(self.pointers) == self.capacity:
                node = self.head.next
                lru = node
                self.remove(lru)    

            self.insert(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)