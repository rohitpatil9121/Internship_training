class listnode:
    def __init__(self, val=0, next=0):
        self.val = val
        self.next = None

node = listnode(10)
node1 = listnode(20)
node2 = listnode(30)
node.next = node1
node1.next = node2

print(node.val)
print(node1.val)
print(node1.val)

head = node
current = head

while current is not None:
    print(current.val, end=" -> ")  
    current = current.next

print("None")
