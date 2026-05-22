class node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None
class MyHashSet:

    def __init__(self):
        self.a=[node(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        i=key%len(self.a)
        c=self.a[i]
        while c.next:
            if c.next.val==key: return
            c=c.next
        c.next=node(key)
    def remove(self, key: int) -> None:
        i=key%len(self.a)
        c=self.a[i]
        while c.next:
            if c.next.val==key:
                c.next=c.next.next
                return
            c=c.next

    def contains(self, key: int) -> bool:
        i=key%len(self.a)
        c=self.a[i]
        while c.next:
            if c.next.val==key:
                return True
            c=c.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)