import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {} # A dictionary to track val: idx
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # print("Insert", self.list, self.dict)
        if val in self.dict:
            return False
        else:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # print("Delete", self.list, self.dict)

        if val not in self.dict or not self.list:
            return False
        else: # Remove it
            idx = self.dict[val]
            temp = self.list[-1]
            self.list[idx] = temp
            self.dict[temp] = idx
            self.list = self.list[:len(self.list) - 1]
            self.dict.pop(val)
            return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # print("getRandom", self.list, self.dict)
        try: 
            idx = random.randint(0, len(self.list)-1)
        except:
            return None
        return self.list[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""
["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
[[],[0],[1],[0],[2],[1],[]]
"""
# obj = RandomizedSet()
# print(obj.getRandom())
# print(obj.insert(0))
# print(obj.insert(1))
# print(obj.remove(0))
# print(obj.insert(2))
# print(obj.remove(1))
# print(obj.getRandom())




