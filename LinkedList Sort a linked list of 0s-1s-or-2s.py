# Python program to remove duplicates from an
# unsorted linked list

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Function to remove duplicates using nested loops
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def sortList(head):

    zeroD = Node(0)
    oneD = Node(0)
    twoD = Node(0)

    zero = zeroD
    one = oneD
    two = twoD

    curr = head
    while curr != None:
        if curr.data == 0:
            zero.next = curr
            zero = zero.next
        elif curr.data == 1:
            one.next = curr
            one = one.next
        else:
            two.next = curr
            two = two.next
        curr = curr.next

    if oneD.next != None:
        zero.next = oneD.next
    else:
        zero.next = twoD.next

    one.next = twoD.next
    two.next = None

    head = zeroD.next
    return head



def countofelements(head):
    curr = head
    while
























if __name__ == "__main__":
    # Create a singly linked list:
    # 12 -> 11 -> 12 -> 21 -> 41 -> 43 -> 21
    head = Node(1)
    head.next = Node(0)
    head.next.next = Node(1)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(0)
    head.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next = Node(2)


    print_list(head)
    head = sortList(head)
    print_list(head)
