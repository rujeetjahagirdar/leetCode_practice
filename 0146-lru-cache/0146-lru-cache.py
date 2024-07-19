class Node:
    def __init__(self, key=None, val=None):
        self.prev = None
        self.next=None
        self.val = val
        self.key = key
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        
        
    def remove(self, node):
        # print("remove")
        node.prev.next = node.next
        node.next.prev = node.prev

        # print(self.cache, self.left.next.val, self.right.prev.val)
    
    def insert(self, node):
        
        self.right.prev.next = node
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev = node

        # print(self.cache, self.left.next.val, self.right.prev.val)
        
        
        
        
    def get(self, key: int) -> int:
        # if key in cache:
            #return the value
            #remove that node
            #insert that node
        #else:
            #return -1
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #if key in cache:
            #remoove node
            #insert new node
        #else
            #if capacity full:
                #remove least used
                #insert new node
            #else:
                #insert new node
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            if len(self.cache)>=self.capacity  :
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
                self.cache[key] = Node(key, value)
                self.insert(self.cache[key])
            else:
                self.cache[key] = Node(key, value)
                self.insert(self.cache[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)