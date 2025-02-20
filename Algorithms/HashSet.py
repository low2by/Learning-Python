# We can use a hash value to compute an index into a list to obtain O(1) item lookup complexity.

class HashSet:
    def __init__(self,contents=[]):
        self.items = [None] * 10
        self.numItems = 0

        for item in contents:
            self.add(item)

    # In this add method, We’ll explore a scheme called Linear Probing. When a
    # collision occurs while using linear probing, we advance to the next location in the
    # list to see if that location might be available.
    def __add(item,items):
        idx = hash(item) % len(items)
        loc = -1

        # linear probing
        while items[idx] != None:
            if items[idx] == item:
            # item already in set
                return False


            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx

            idx = (idx + 1) % len(items)

        if loc < 0:
            loc = idx

        items[loc] = item

        return True
    
    def __rehash(oldList, newList):
        for x in oldList:
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x,newList)

        return newList

    def add(self, item):
        if HashSet.__add(item,self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
        # if the resulting load factor is greater than 75% then all the values
        # in the list must be transferred to a new list. To transfer the values to a new list the
        # values must be hashed again because the new list is a different length. This process
        # is called rehashing. In    
        if load >= 0.75: 
            self.items = HashSet.__rehash(self.items,[None]*2*len(self.items))

    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self,other):
            return False

    def __remove(item,items):
        idx = hash(item) % len(items)

        while items[idx] != None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                if items[nextIdx] == None:
                    items[idx] = None
                else:
                    # If the value to be deleted is the last in a chain then it can be replaced with a None. If it is in the
                    # middle of a chain then we cannot replace it with None because this would cut the
                    # chain of values. Instead, the item is replaced with a __Placeholder object. A place
                    # holder object does not break a chain and a linear probe continues to search skipping
                    # over placeholder objects when necessary
                    items[idx] = HashSet.__Placeholder()
                return True

            idx = (idx + 1) % len(items)

        return False
    
    def remove(self, item):
        if HashSet.__remove(item,self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)

            #When removing an item, the load factor may get too low to be efficiently using
            # space in memory. When the load factor dips below 25%, the list is again rehashed to
            # decrease the list size by one half to increase the load factor
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items,[None]*int(len(self.items)/2))
        else:
            raise KeyError("Item not in HashSet")
    
    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return True

            idx = (idx + 1) % len(self.items)

        return False
    
    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]

    def __getitem__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return self.items[idx]

            idx = (idx + 1) % len(self.items)
        return None
    
    