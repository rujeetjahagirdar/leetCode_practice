class Node:
    def __init__(self, key = None, val = None, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        #initialize capacity
        #initialize cache
        #initialize double linke list
        self.capacity = capacity
        self.cache = {} #key:node
        self.head = Node() #dummy node for head
        self.tail = Node() #dummy node for tail, actual nodes will be in between these two nodes
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def removeNode(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    
    def addNode(self, node):
        prv, nxt = self.tail.prev, self.tail
        prv.next = node
        nxt.prev = node
        node.prev = prv
        node.next = nxt

    def get(self, key: int) -> int:
        if(key not in self.cache):
            return -1
        else:
            n = self.cache[key]
            self.removeNode(n)
            del self.cache[n.key]

            self.put(n.key, n.val)

            return n.val

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            self.removeNode(self.cache[key])
            del self.cache[key]
        
        newNode = Node(key=key, val=value)
        self.addNode(newNode)
        self.cache[newNode.key] = newNode

        if(len(self.cache)>self.capacity):
            most_recently_used = self.head.next
            self.removeNode(most_recently_used)
            del self.cache[most_recently_used.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)