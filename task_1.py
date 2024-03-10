class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def unshift(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            end = " => " if current.next else ""
            print(current.data, end=end)
            current = current.next
        print()

    def reverse(self):
        """написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;"""
        prev = None
        current = self.head

        while current:
            # запамʼятали, який вузол буде ннаступним, бо зараз затремо посилання
            next_node = current.next
            # реверснули посилання на поточному вузлі
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


def merge_lists(llist1, llist2):
    """функція, об'єднання двох списків в один"""
    llist = LinkedList()
    llist.head = merge(llist1.head, llist2.head)
    return llist


def merge(llist1, llist2):
    """функція, об'єднання"""
    llist = Node()
    current = llist

    while llist1 and llist2:
        if llist1.data < llist2.data:
            current.next = llist1
            llist1 = llist1.next
        else:
            current.next = llist2
            llist2 = llist2.next
        current = current.next

    if llist1:
        current.next = llist1
    else:
        current.next = llist2

    return llist.next


def get_middle(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_sort_list(llist):
    linkedList = LinkedList()
    linkedList.head = merge_sort(llist.head)
    return linkedList


def merge_sort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    middle_next = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(middle_next)
    llist = merge(left, right)

    return llist


def main():
    print("Створюємо однозв'язний список")
    linkedList = LinkedList()

    print("Добавляємо вузли на початок: 3, 11, 12")
    linkedList.unshift(3)
    linkedList.unshift(11)
    linkedList.unshift(12)

    print("Добавляємо вузли у кінець: 22, 26")
    linkedList.append(22)
    linkedList.append(26)

    print("Вузли до реверсування:")
    linkedList.print_list()

    print("Робимо реверсування")
    linkedList.reverse()

    print("Вузли після реверсування:")
    linkedList.print_list()

    print("Робимо сортування")
    linkedList = merge_sort_list(linkedList)
    linkedList.print_list()

    print()
    print("Об'єднання двох однозв'язних списків")
    print("Створюємо перший однозв'язний список з вузлами: 1, 3, 5")
    linkedList1 = LinkedList()
    linkedList1.append(1)
    linkedList1.append(3)
    linkedList1.append(5)
    linkedList1.print_list()

    print("Створюємо другий однозв'язний список з вузлами: 2, 4, 6")
    linkedList2 = LinkedList()
    linkedList2.append(2)
    linkedList2.append(4)
    linkedList2.append(6)
    linkedList2.print_list()

    print("Робимо обʼєднання")
    linkedList3 = merge_lists(linkedList1, linkedList2)
    linkedList3.print_list()


if __name__ == "__main__":
    main()
