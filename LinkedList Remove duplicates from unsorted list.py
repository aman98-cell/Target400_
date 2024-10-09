# Python program to remove duplicates from an
# unsorted linked list

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Function to remove duplicates using nested loops
def remove_duplicates(head):
    prev = None
    curr = head
    emptyset  = set()

    while curr != None:
        if curr.data in emptyset:
            prev.next = curr.next
            curr = curr.next
        else:
            emptyset.add(curr.data)
            prev = curr
            curr = curr.next
    return head




def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    # Create a singly linked list:
    # 12 -> 11 -> 12 -> 21 -> 41 -> 43 -> 21
    head = Node(12)
    head.next = Node(11)
    head.next.next = Node(12)
    head.next.next.next = Node(21)
    head.next.next.next.next = Node(41)
    head.next.next.next.next.next = Node(43)
    head.next.next.next.next.next.next = Node(21)


    print_list(head)
    head = remove_duplicates(head)
    print_list(head)