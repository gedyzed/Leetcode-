class Node:
    def __init__(self, url="", prev=None, next=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:

        new_node = Node(url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = new_node

    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            steps -= 1
            self.curr = self.curr.prev

        return self.curr.url    

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.url    
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)