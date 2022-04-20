class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

def union(llist_1, llist_2):
    # Your Solution Here
    temp_set = set()
    llist_union = LinkedList()

    if  llist_1.size() == 0 and llist_2.size() == 0:
        return None

    for value in llist_1:
        temp_set.add(value)

    for value in llist_2:
        temp_set.add(value)

    for temp_val in temp_set:
        llist_union.append(temp_val)

    return llist_union

def intersection(llist_1, llist_2):
    # Your Solution Here
    temp_set = set()
    llist_intersection = LinkedList()
    
    if llist_1.size() == 0 or llist_2.size() == 0:
        return None

    for value in llist_1:
        if value in llist_2:
            temp_set.add(value)

    for value in temp_set:
        llist_intersection.append(value)

    if llist_intersection.size() == 0:
        return None
    else:    
        return llist_intersection

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

#Test case 3

element_3 = []
element_4 = [0, 8, 0, 7]

for i in element_3:
    linked_list_5.append(i)

for i in element_4:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_6,linked_list_5))