class HashTableEntry:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        
class HashMapTable:
    def __init__(self):
        self.table = [None] * T_S
        
    def hash_func(self, k):
        return k % T_S
        
    def insert(self, k, v):
        h = self.hash_func(k)
        while self.table[h] is not None and self.table[h].key != k:
            h = self.hash_func(h + 1)
        if self.table[h] is not None:
            del self.table[h]
        self.table[h] = HashTableEntry(k, v)
        
    def search_key(self, k):
        h = self.hash_func(k)
        while self.table[h] is not None and self.table[h].key != k:
            h = self.hash_func(h + 1)
        if self.table[h] is None:
            return -1
        else:
            return self.table[h].value
        
    def remove(self, k):
        h = self.hash_func(k)
        while self.table[h] is not None:
            if self.table[h].key == k:
                break
            h = self.hash_func(h + 1)
        if self.table[h] is None:
            print("No Element found at key ", k)
            return
        else:
            del self.table[h]
        print("Element Deleted")
