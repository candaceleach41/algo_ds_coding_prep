"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise,
add the key-value pair to the cache. If the number of keys exceeds the capacity from this
operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""

class Node:
    def __init__(self, value, key, next=None, prev=None):
        self.value = value
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def put(self, key, value):
        if key not in self.cache:
            # Invalidate oldest if required:
            if len(self.cache) == self.capacity:
                del self.cache[self.head.key]
                self.remove_head()
            node = Node(key, value)
            self.cache[key] = node
        else:
            # Update the value:
            node = self.cache[key]
            node.value = value
        self.make_most_recent(node)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.make_most_recent(node)
            return node.value
        else:
            return -1

    def remove_head(self):
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def make_most_recent(self, node):
        if self.head and self.head.key == node.key:
            self.remove_head()
            # Make this item the most recently accessed (tail):
        if self.tail and not self.tail.key == node.key:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            node.next = None
            self.tail.next = node  # Old tail's next is the node.
            node.prev = self.tail  # Node's previous is the old tail.
        self.tail = node  # New tail is the node.
        if not self.head:
            self.head = node  # If this is the first item make it the head as well as tail.


if __name__ == "__main__":
    lru = LRUCache(3)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.get(1)
    lru.put(3, 3)
    lru.put(4, 4)
    lru.get(1)
    lru.get(2)
    lru.put(5, 5)
    lru.get(3)
