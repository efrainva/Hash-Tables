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
        # self.length = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        print(hash(key))
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):

        # this doesn't put anything in order
        # self.head = self.capacity -1 # the 'head starts from the right side
        # hash(key)
        # cap = self.capacity
        # for i in range(cap-1 , 0 ,-1):
        #     # print(i, i-1 )
        #     self.storage[ i] = self.storage[i -1 ]
        # #   print(i , i-1)

        # pair = {hash(key):value}
        # self.storage[0] = pair
        # print(self.storage)
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            print('Collision for key '+ key)
        self.storage[index] = LinkedPair(key,value)



    def get(self):
        print( self.storage )
        return


    def remove(self, key):
        # for i in self.storage:
        #     if i == key:
        #         self.storage[i] = None
        #         print(self.storage[i])
        #     else:
        #         print('no key or wrong key')
        index = self._hash_mod(key)
        self.storage[index] = None

    def retrieve(self, key):

        # hkey = hash(key)
        # print(hkey,'107')
        # for i in range(0, self.capacity-1):
        #     if self.storage[i].get(hkey) != hkey:
        #         print(self.storage[i].get(hash(key)))
        #     else:
        #         None

        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        return self.storage[index].value

    def resize(self):
        cap = self.capacity *2
        print(cap )
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # pass
 
# one = HashTable(5)
# one.resize()


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