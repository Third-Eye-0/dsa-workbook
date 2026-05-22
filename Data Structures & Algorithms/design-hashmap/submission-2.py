class node:
    def __init__(self,key=-1, value=-1, next=None):
        self.key=key
        self.value=value
        self.next=next

class MyHashMap:

    def __init__(self):
        self.a=[node() for i in range(1000)]
    def hash(self, key):
        return key%len(self.a)

    def put(self, key: int, value: int) -> None:
        c=self.a[self.hash(key)]
        while c.next:
            if c.next.key==key:
                c.next.value=value
                return
            c=c.next
        c.next=node(key,value)

    def get(self, key: int) -> int:
        c=self.a[self.hash(key)]
        while c.next:
            if c.next.key==key:
                return c.next.value
            c=c.next
        return -1

        

    def remove(self, key: int) -> None:
        c=self.a[self.hash(key)]
        while c.next:
            if c.next.key==key:
                c.next=c.next.next
                return
            c=c.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)