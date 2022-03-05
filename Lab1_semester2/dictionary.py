class HashMap:
    # Class for linked list`s nodes
    class Node:
        def __init__(self, value, key, next_node=None):
            self.value = value
            self.key = key  # key for dictionary is stored here
            self.next = next_node

    # Linked list`s class
    class LinkedList:
        def __init__(self):
            self.head = None
            self.end = None

        # method to insert new node in the end
        def insert_at_end(self, value, key):
            if self.head is None:
                self.head = self.end = HashMap.Node(value, key)
            else:
                self.end.next = self.end = HashMap.Node(value, key)

        # method for formatting LinkedList
        def __str__(self):
            if self.head is not None:
                current = self.head
                result = f'[{current.value}, '
                while current.next is not None:
                    current = current.next
                    result += f'{current.value}, '
                result = result[:-2]
                result += f']'
                return result
            return '[]'

    # initializing dictionary
    def __init__(self, n=10):
        self._inner_list = [None] * n
        self._size = n  # attribute to store length
        self._cnt = 0   # attribute to store how many elements were added

    # getting item by key
    def __getitem__(self, key):
        linklist = self._inner_list[hash(key) % self._size]
        current = linklist.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

    # setting element by magic method
    def __setitem__(self, key, value):
        index = hash(key) % self._size
        if self._inner_list[index] is None:
            self._inner_list[index] = HashMap.LinkedList()
            self._inner_list[index].insert_at_end(value, key)
        else:
            lst = self._inner_list[index]
            current = lst.head
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            lst.insert_at_end(value, key)
        self._cnt += 1
        # if number of elements in dict is 90% of size, increasing size
        if self._cnt >= 0.9 * self._size:
            self._size = self._size * 17 // 10  # increasing by 1.7 to make more random indexes
            new_inner_list = [None] * self._size
            for linlist in self._inner_list:
                if linlist is not None:
                    current = linlist.head
                    while current is not None:
                        index = hash(current.key) % self._size
                        if new_inner_list[index] is None:
                            new_inner_list[index] = HashMap.LinkedList()
                            new_inner_list[index].insert_at_end(current.value, current.key)
                        else:
                            lst = new_inner_list[index]
                            curr = lst.head
                            while curr is not None:
                                if curr.key == key:
                                    curr.value = value
                                    return
                                curr = curr.next
                            lst.insert_at_end(value, key)
                        current = current.next
            self._inner_list = new_inner_list

    # __str__ is made to return only values
    def __str__(self):
        return '[' + ', '.join(map(str, self._inner_list)) + ']'


hm = HashMap()
hm[14] = 1
hm[4] = 2
hm[4] = 5
hm[9] = 1
hm[8] = 1
hm[7] = 1
hm[6] = 1
hm[5] = 1
hm[3] = 1
print(hm)   # here dict`s length is 10
hm[2] = 1
hm[1] = 1
hm[0] = 9
hm[10] = 8
print(hm[10])
print(hm[14])
print(hm)   # here dict`s length is 17
