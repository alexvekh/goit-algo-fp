"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""

class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
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
      print(current.data, end=" ")
      current = current.next
  
  # реверсування однозв'язного списку, змінюючи посилання між вузлами  ---------------------------------
  def reverse(self):
    cur = self.head
    prev = None
    next = cur.next
    while cur.next:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
    self.head = cur
    cur.next = prev

  # сортування вставками однозв'язного списку  ---------------------------------------------------------  
  def sort(self):
    if self.head is None or self.head.next is None:
      return self  # Empty or single-element list is already sorted
    sorted_end = self.head
    # move sorted part if next is biger
    while sorted_end.next:
      if sorted_end.data <= sorted_end.next.data:
        sorted_end = sorted_end.next
      else:     # take off if next is smaller
        taked_node = sorted_end.next
        sorted_end.next = taked_node.next 
        
        # if smaller for head, insert before head
        if self.head.data > taked_node.data:
          taked_node.next = self.head
          self.head = taked_node
        
        # if biger for head - compare with next
        else:
          cur = self.head
          while cur.next.data <= taked_node.data:
            cur = cur.next

          # insert before next
          taked_node.next = cur.next
          cur.next = taked_node

    return self


# функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список.----------------------
def merge_linked_lists(list: LinkedList, second_list: LinkedList):
  lists = [list, second_list]   # Буде легко змінити на merge-k-lists
  merged_list = LinkedList()
  for list in lists:
    node = list.head
    while node:
      if not merged_list.head or node.data < merged_list.head.data:
        merged_list.insert_at_beginning(node.data)
      else:
        cur = merged_list.head
        while cur.next and cur.next.data <= node.data:
          cur = cur.next
        merged_list.insert_after(cur, node.data)
      node = node.next          

  return merged_list






llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
# llist.insert_at_beginning(40)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("\n  Linked list:")
llist.print_list()

# Видаляємо вузол
# llist.delete_node(10)

# print("\nЗв'язний список після видалення вузла з даними 10:")
# llist.print_list()

# Пошук елемента у зв'язному списку
# print("\nШукаємо елемент 15:")
# element = llist.search_element(15)
# if element:
#   print(element.data)

llist.reverse()
print("\n  Reversed linked list function demo:")
llist.print_list()

llist.sort()
print("\n  Sorted linked list function demo:")
llist.print_list()



# merging sort
one_list = LinkedList()
one_list.insert_at_beginning(5)
one_list.insert_at_end(3)
one_list.insert_at_end(7)
one_list.insert_at_end(1)
one_list.insert_at_end(40)

other_list = LinkedList()
other_list.insert_at_beginning(6)
other_list.insert_at_end(2)
other_list.insert_at_end(8)
other_list.insert_at_end(16)

print("\n  2 linked lists merging demo: ")
print("\nOne list:")
one_list.print_list()
print("\nOther list:")
other_list.print_list()

merged = merge_linked_lists(one_list, other_list)
print("\nMerged and sorted:")
merged.print_list()