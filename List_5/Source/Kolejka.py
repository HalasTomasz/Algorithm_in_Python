from collections import namedtuple

NodeList = namedtuple('NodeList', ['key', 'priority'])

def parent(i: int):
    return i // 2

def left(i: int):
    return 2 * i

def right(i: int):
    return 2 * i + 1


class Kolejka():

    def __init__(self, MyData=[]):
         self.__heap = MyData
         for i in range((len(MyData)-1)//2, -1, -1):
             self.__heapify(i)

    def insert(self, key, priority):
        
        new_node = NodeList(key=key, priority=priority)
        heap = self.__heap
        heap.append(new_node)
        i = len(heap)-1
        if i != -1:
            while i > 0 and heap[parent(i)].priority > new_node.priority:
                heap[i] = heap[parent(i)]
                i = parent(i)
        heap[i] = new_node

    def delete(self, i):
        heap = self.__heap
        lost = heap[i]
        heap[i] = heap[-1]
        del heap[-1]
        if not self.is_empty() and i != len(heap):
            self.__heapify(i)
        return lost
    
    def heap(self):
        return self.__heap

    def __heapify(self, i):
   
        heap = self.__heap
        data = list(filter(lambda x: x < len(heap), [i, left(i), right(i)]))
        abc = data[list(map(lambda x: self.__heap[x].priority, data)).index(min(list(map(lambda x: self.__heap[x].priority, data))))]
        if abc != i:
            heap[i], heap[abc] = heap[abc], heap[i]
            self.__heapify(abc)

    def is_empty(self):
        return len(self.__heap) == 0

    def top(self):
        return self.__heap[0]

    def pop(self):
        return self.delete(0)

    def priority(self, key, new_priority):
        heap = self.__heap
        counter = 0
        length = len(heap)
        i = 0
        while i < length:
            if heap[i].key == key and heap[i].priority > new_priority:
                counter += 1
                self.delete(i)
                i = -1
                length -= 1
            i += 1

        for x in range(counter):
            self.insert(key, new_priority)