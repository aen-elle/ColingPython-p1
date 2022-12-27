class MinStack:

    def __init__(self):
        self.stack = []
        self.min_el = []
        self.previous_mins = []

    def push(self, val: int):
        self.stack.append(val)
        if self.min_el:
            if val < self.min_el[0]:
                self.previous_mins.append(self.min_el[0])
                self.min_el[0] = val
        else:
            self.min_el.append(val)
        

    def pop(self):
        if self.stack[-1] == self.min_el[0]:
            self.min_el[0] = self.previous_mins[-1]
        self.stack.pop(-1)
        

    def top(self):
        return self.stack[-1]
        
        

    def getMin(self):
        if self.stack:
            return self.min_el[0]



