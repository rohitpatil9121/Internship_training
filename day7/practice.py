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

#206
#reverse linked list
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev

#203
#remove linked list elements
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

class solution:
    def removeElements(self, head, val):
        dummy = listnode(0)
        dummy.next = head
        prev = dummy

        while head is not None:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next

        return dummy.next