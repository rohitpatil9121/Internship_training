# for j in range(11,50):
#     flag = True
#     for i in range(2,j):
#         if j % i == 0:
#             flag = False
#             break

#     if flag:
#         print("prime:", j)

#     else:
#         print("not prime:", j)       

class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addtwonumbers(l1,l2):
    dummy = listnode(0)
    current = dummy
    carry = 0

    while l1 or l2:

        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

    sum = x + y + carry

    carry = sum // 10
    current.next = listnode(sum % 10)
    current = current.next

    if l1:
        l1 = l1.next
    if l2:
        l2 = l2.next

if carry>0:
    current.next = listnode(carry)

return dummy.next
