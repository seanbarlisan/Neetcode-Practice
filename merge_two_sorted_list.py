# class Node: # Initialization for linked list node class
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

# def printList(head): # print the data
    
#     while head is not None:
#         print(f"{head.data} -> ", end="")
#         head = head.next
#     print("nullptr")

def ListNodePrintList(head):
    while head is not None:
        print(f"{head.val} -> ", end="")
        head = head.next
    print("nullptr")

# def mergeList(list1, list2): # Not optiomal, uses nlogm needs to be O(n)
#     arr = []

#     while list1 is not None:
#         arr.append(list1.data)
#         list1 = list1.next

#     while list2 is not None:
#         arr.append(list2.data)
#         list2 = list2.next

#     arr.sort()

#     dummy = Node(-1)
#     curr = dummy

#     for value in arr:
#         curr.next = Node(value)
#         curr = curr.next

#     return dummy.next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    node.next = list1 or list2

    return dummy.next

if __name__ == "__main__":
    # list1 = Node(10)
    # list1.next = Node(20)
    # list1.next.next = Node(30)

    # list2 = Node(10)
    # list2.next = Node(40)
    # list2.next.next = Node(50)

    # print("This is List 1:\n")
    # printList(list1)

    # print("This is List 2:\n")
    # printList(list2)

    # print("This is a Merged List:\n")
    # res = mergeList(list1, list2)
    # printList(res)

    list1 = ListNode(10)
    list1.next = ListNode(20)
    list1.next.next = ListNode(30)

    list2 = ListNode(10)
    list2.next = ListNode(40)
    list2.next.next = ListNode(50)

    res = mergeTwoLists(list1, list2)
    ListNodePrintList(res)