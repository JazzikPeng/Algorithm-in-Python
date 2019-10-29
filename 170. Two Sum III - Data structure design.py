class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = collections.Counter()
        self.minVal = float('inf')
        self.maxVal = float('-inf')
        
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums[number] += 1
        self.minVal = min(self.minVal, number)
        self.maxVal = max(self.maxVal, number)
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if value < self.minVal * 2 or value > self.maxVal * 2:
            return False
        for num in self.nums:
            # Numbers are saved as a dictionary. This steps is checking if self.nums[num] contain more than one element 
            # So there are two number add to value. Or the value is a sum of two different number.
            if value - num in self.nums and (self.nums[num] > 1 or value-num!=num): 
                return True
        return False
                
                
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)