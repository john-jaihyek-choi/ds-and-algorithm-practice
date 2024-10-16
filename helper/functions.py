class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, list: list) -> None:
        self.head: ListNode = self._link_nodes(list)

    def _link_nodes(self, list: list) -> ListNode:
        prev = None

        for i in range(len(list) - 1, -1, -1):
            new_node = ListNode(list[i], prev)
            prev = new_node

        return prev

class Utility:
    @staticmethod
    def print_linked_list(head: ListNode) -> None:
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")