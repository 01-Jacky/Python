import random, string


class Node:
    """ Helper class to create linked list"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


class HashTable:
    """
    An overflow-chaining implementation of hashtable
    Each bin points to the head of a linked list
    All linked list are trailer linked list to make deletion easier (there's always an empty node at the end).
        i.e. deletion works by copying next Node's value and next pointer into the current node
    """
    def __init__(self, size=10):
        self.size = 0
        self.bins = [Node(None)] * size

    # Queries
    def get(self, key):
        """ return the value associated with the given key, or null if no value is set """
        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        node = self._find_node(key)
        if node is None:
            return None
        else:
            return node.value[1]

    def delete(self, key):
        """ delete the value associated with the given key, returning the value on success or null if the key has no value """
        node_to_delete = self._find_node(key)
        if node_to_delete is None:
            return None
        else:
            # Using linked list with trailer node allows us to do use this trick to delete current node easily
            # without checking if the node is the last one
            deleted_value = node_to_delete.value[1]
            node_to_delete.value = node_to_delete.next.value
            node_to_delete.next = node_to_delete.next.next
            self.size -= 1
            if self.size < 0:
                raise ValueError("size fell below 0")

            return deleted_value

    def load(self):
        return self.size/float(len(self.bins))           # Don't necessary need this in Python 3

    # Commands
    def set(self, key, value):
        if self.load() >= 1:
            raise ValueError("Load is above 1 for this fixed sized hash table. Failed to insert")
        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        bin_num = self._get_bin(key)
        cur = self.bins[bin_num]

        if cur.next is None:
            self.bins[bin_num] = Node((key, value), cur)
        else:
            while cur.next is not None:
                prev = cur
                cur = cur.next
            prev.next = Node((key, value), cur)

        self.size += 1
        return True

    # Helpers
    def _hash(self, key):
        hash_code = 0
        for char in key:
            hash_code += 31*hash_code + ord(char)    # 31 as multiplier because of odd prime (may help with some optimization)
        return hash_code

    def _get_bin(self, key):
        return self._hash(key) % len(self.bins)

    def _find_node(self, key):
        bin_num = self._get_bin(key)
        cur = self.bins[bin_num]

        while cur.next is not None:
            if cur.value[0] == key:
                return cur
            cur = cur.next

        return None

    def _printBins(self):
        for i in range(len(self.bins)):
            s = "Bin #" + str(i) + ': '

            cur = self.bins[i]
            if cur.next is not None:
                while cur.next is not None:
                    s += '({}, {})'.format(cur.value[0], cur.value[1])
                    cur = cur.next
            print(s)
            i += 1



if __name__ == '__main__':

    hashmap = HashTable()
    print(hashmap.set('wtf',230))

    for x in range(9):
        hashmap.set(
            ((random.choice(string.ascii_letters + string.digits))+(random.choice(string.ascii_letters + string.digits)))
            , random.randint(0,100))
    hashmap._printBins()

    found_node = hashmap._find_node('wtf')
    if found_node is None:
        print('not found')
    else:
        print(found_node.value)

    print(hashmap.delete("wtf"))
    hashmap._printBins()