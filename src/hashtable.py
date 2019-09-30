# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        n = 5381

        for character in key:
            n = n * 33 + ord(character)

        return n % 2**64

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        # Normal hash. Success.
        # return self._hash(key) % self.capacity

        # DJB2 hash. Success.
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)

        new_pair = LinkedPair(key, value)

        if self.storage[index]:
            current_node = self.storage[index]

            if current_node.key == key:
                current_node.value = value
            else:
                missing = True
                next_node = current_node.next

                while next_node:
                    current_node = next_node
                    next_node = current_node.next

                    if current_node.key == key:
                        current_node.value = value
                        missing = False

                if missing is True:
                    current_node.next = new_pair
        else:
            self.storage[index] = new_pair


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index]:
            current_node = self.storage[index]

            if current_node.key == key:
                self.storage[index] = current_node.next
            else:
                next_node = current_node.next

                while next_node:
                    prev_node = current_node
                    current_node = next_node
                    next_node = current_node.next

                    if current_node.key == key:
                        prev_node.next = next_node


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index]:
            current_node = self.storage[index]

            if current_node.key == key:
                return current_node.value
            else:
                next_node = current_node.next

                while next_node:
                    current_node = next_node
                    next_node = current_node.next

                    if current_node.key == key:
                        return current_node.value
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = 2 * len(self.storage)
        self.storage = [None] * self.capacity

        for i in range(0, len(old_storage)):
            if old_storage[i]:
                current_node = old_storage[i]
                self.insert(current_node.key, current_node.value)

                next_node = current_node.next
                while next_node:
                    self.insert(next_node.key, next_node.value)
                    current_node = next_node
                    next_node = current_node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
